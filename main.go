package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"image"
	"io/ioutil"
	"log"
	"net/http"
	"os"

	"gocv.io/x/gocv"
)

func save_all_frames(video_path string) []string {
	cap, err := gocv.VideoCaptureFile(video_path)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(video_path)

	if !cap.IsOpened() {
		fmt.Println("Cannot Open")
	}
	fmt.Println("OK")
	n := 0
	frame := gocv.NewMat()
	defer frame.Close()
	var frame_list []gocv.Mat
	for cap.Read(&frame) {
		if n%5 == 0 {
			frame_list = append(frame_list, frame.Clone())
		}
	}
	fmt.Println(frame.Size())
	return convertToASCII(&frame_list)
}

func convertToASCII(frame_list *[]gocv.Mat) []string {
	var result []string
	fmt.Println("ConvertStart")
	colorset := "MWN$@%#&B89EGA6mK5HRkbYT43V0JL7gpaseyxznocv?jIftr1li*=-~^`':;,. "
	for ind, frame := range *frame_list {
		var frame_string string
		_, width := frame.Size()[0], frame.Size()[1]
		scale_ratio := 1.0
		if width >= 400 {
			scale_ratio = 400.0 / float64(width)
		}
		gocv.Resize(frame, &frame, image.Point{}, scale_ratio, scale_ratio, gocv.InterpolationArea)
		height, width := frame.Size()[0], frame.Size()[1]
		frame.ConvertTo(&frame, gocv.MatTypeCV8U)
		gocv.CvtColor(frame, &frame, gocv.ColorBGRAToGray)
		for h := 0; h < height; h++ {
			for w := 0; w < width; w++ {
				frame_string += string(colorset[frame.GetUCharAt(h, w)/4]) + string(colorset[frame.GetUCharAt(h, w)/4])
			}
			frame_string += "<br>"
		}
		result = append(result, frame_string)
		fmt.Println(ind)
	}
	return result
}

func api(w http.ResponseWriter, r *http.Request) {
	// fmt.Fprintf(w, "Welcome to the HomePage!")
	file, _, err := r.FormFile("video")
	fmt.Println("Welcome to the HomePage!")
	if err != nil {
		fmt.Println(err)
		return
	}
	defer file.Close()
	tmpFile, _ := ioutil.TempFile("/tmp", "tmptest")
	tmpfileName := tmpFile.Name()
	defer tmpFile.Close()
	defer os.Remove(tmpfileName)
	fileBytes, err := ioutil.ReadAll(file)
	if err != nil {
		fmt.Println(err)
	}
	tmpFile.Write(fileBytes)
	var buf bytes.Buffer
	enc := json.NewEncoder(&buf)
	pj := save_all_frames(tmpfileName)
	if err := enc.Encode(&pj); err != nil {
		log.Fatal(err)
	}
	fmt.Fprint(w)
}

func handleRequests() {
	http.HandleFunc("/api", api)
	log.Fatal(http.ListenAndServe(":8000", nil))
}

func main() {

	//ディレクトリを指定する
	//ルーティング設定。"/"というアクセスがきたらstaticディレクトリのコンテンツを表示させる
	fs := http.FileServer(http.Dir("static"))
	http.Handle("/", fs)
	http.HandleFunc("/api", api)

	log.Println("Listening...")
	// 3000ポートでサーバーを立ち上げる
	http.ListenAndServe(":8000", nil)
}
