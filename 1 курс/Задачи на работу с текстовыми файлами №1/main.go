package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	//1
	file, _ := os.Open("numbers.txt")
	scanner := bufio.NewScanner(file)
	sum, count := 0.0, 0
	for scanner.Scan() {
		num, _ := strconv.ParseFloat(scanner.Text(), 64)
		sum += num
		count++
	}
	fmt.Printf("Среднее: %.2f\n", sum/float64(count))
	file.Close()

	//2
	file, _ = os.Open("numbers.txt")
	scanner = bufio.NewScanner(file)
	scanner.Scan()
	min, _ := strconv.ParseFloat(scanner.Text(), 64)
	max := min
	for scanner.Scan() {
		num, _ := strconv.ParseFloat(scanner.Text(), 64)
		if num < min {
			min = num
		}
		if num > max {
			max = num
		}
	}
	fmt.Printf("Min: %.2f\nMax: %.2f\n", min, max)
	file.Close()

	//3
	in, _ := os.Open("numbers.txt")
	out, _ := os.Create("even_numbers.txt")
	scanner = bufio.NewScanner(in)
	for scanner.Scan() {
		num, _ := strconv.Atoi(scanner.Text())
		if num%2 == 0 {
			out.WriteString(fmt.Sprintf("%d ", num))
		}
	}
	in.Close()
	out.Close()

	//4
	file, _ = os.Open("text.txt")
	scanner = bufio.NewScanner(file)
	lines := 0
	for scanner.Scan() {
		lines++
	}
	fmt.Printf("Строк: %d\n", lines)
	file.Close()

	//5
	file, _ = os.Open("My_text.txt")
	scanner = bufio.NewScanner(file)
	words := 0
	for scanner.Scan() {
		words += len(strings.Fields(scanner.Text()))
	}
	fmt.Printf("Слов: %d\n", words)
	file.Close()

	//6
	filename := "text.txt"
	print("Введите слово для замены: ")
	var oldWord string
	_, _ = fmt.Scan(&oldWord)
	print("Введите новое слово: ")
	var newWord string
	_, _ = fmt.Scan(&newWord)
	data, _ := os.ReadFile(filename)
	content := string(data)
	updatedContent := strings.ReplaceAll(content, oldWord, newWord)
	_ = os.WriteFile(filename, []byte(updatedContent), 0644)

}
