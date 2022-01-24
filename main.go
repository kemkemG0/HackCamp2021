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
	"unsafe"

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
			fmt.Println(unsafe.Sizeof(frame))
		}
		n += 1
	}
	fmt.Println(frame.Size())
	return convertToASCII(&frame_list)
}

func convertToASCII(frame_list *[]gocv.Mat) []string {
	var result []string
	fmt.Println("ConvertStart")
	colorset := "MWN$@%#&B89EGA6mK5HRkbYT43V0JL7gpaseyxznocv?jIftr1li*=-~^`':;,. "
	_, width := (*frame_list)[0].Size()[0], (*frame_list)[0].Size()[1]
	scale_ratio := 1.0
	if width >= 400 {
		scale_ratio = 400.0 / float64(width)
	}
	for ind, frame := range *frame_list {
		var byte_buf bytes.Buffer
		gocv.Resize(frame, &frame, image.Point{}, scale_ratio, scale_ratio, gocv.InterpolationArea)
		height, width := frame.Size()[0], frame.Size()[1]

		frame.ConvertTo(&frame, gocv.MatTypeCV8U)
		gocv.CvtColor(frame, &frame, gocv.ColorBGRAToGray)

		for h := 0; h < height; h++ {
			for w := 0; w < width; w++ {
				byte_buf.WriteString(string(colorset[frame.GetUCharAt(h, w)/4]) + string(colorset[frame.GetUCharAt(h, w)/4]))
			}
			byte_buf.WriteString("<br>")
		}
		result = append(result, byte_buf.String())
		fmt.Println(ind)
		frame.Close()
	}
	return result
}

type MyRes struct {
	Status int      `json:"status"`
	Art    []string `json:"art"`
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
	data := MyRes{Art: save_all_frames(tmpfileName), Status: 200}

	var buf bytes.Buffer
	enc := json.NewEncoder(&buf)
	if err := enc.Encode(&data); err != nil {
		log.Fatal(err)
	}
	w.Header().Set("Content-Type", "application/json;charset=utf-8")
	_, err = fmt.Fprint(w, buf.String())
	if err != nil {
		fmt.Println(err)
		return
	}
}

func handleRequests() {
	http.HandleFunc("/api", api)
	log.Fatal(http.ListenAndServe(":8000", nil))
}

func main() {

	fs := http.FileServer(http.Dir("static"))
	http.Handle("/", fs)
	http.HandleFunc("/api", api)
	log.Println("Listening...")
	http.ListenAndServe(":8000", nil)
}
