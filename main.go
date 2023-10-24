package main

import "fmt"



func read_line_file(path_file string)  {
	fmt.Printf("Abrindo o arquivo %s",path_file)
}


func main(){

	// Abrindo os arquivos
	read_line_file("teste.txt")
}