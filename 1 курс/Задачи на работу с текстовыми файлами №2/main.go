package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"sort"
	"strings"
)

var stopWords = map[string]bool{
	"и":  true,
	"в":  true,
	"на": true,
	"с":  true,
	"по": true,
}

func getNormalForm(word string) string {
	return strings.ToLower(word)
}

func splitWords(text string) []string {
	reg := regexp.MustCompile(`[^а-яё\s]`)
	cleaned := reg.ReplaceAllString(strings.ToLower(text), "")

	return strings.Fields(cleaned)
}

func part1() {
	file, err := os.Open("text_1.txt")
	if err != nil {
		log.Fatalf("Не удалось открыть файл: %v", err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var text string
	for scanner.Scan() {
		text += scanner.Text() + " "
	}

	if err := scanner.Err(); err != nil {
		log.Fatalf("Ошибка при чтении файла: %v", err)
	}

	words := splitWords(text)
	freq := make(map[string]int)

	for _, word := range words {
		if stopWords[word] {
			continue
		}

		normalForm := getNormalForm(word)
		freq[normalForm]++
	}

	type wordCount struct {
		word  string
		count int
	}

	var sortedWords []wordCount
	for word, count := range freq {
		sortedWords = append(sortedWords, wordCount{word, count})
	}

	sort.Slice(sortedWords, func(i, j int) bool {
		return sortedWords[i].count > sortedWords[j].count
	})

	fmt.Println("Часть 1: Частота слов")
	for i, wc := range sortedWords {
		if i >= 20 {
			break
		}
		fmt.Printf("%s: %d\n", wc.word, wc.count)
	}
}

func part2() {
	process := func(filename string) map[string]bool {
		file, err := os.Open(filename)
		if err != nil {
			log.Fatalf("Не удалось открыть файл %s: %v", filename, err)
		}
		defer file.Close()

		scanner := bufio.NewScanner(file)
		var text string
		for scanner.Scan() {
			text += scanner.Text() + " "
		}

		if err := scanner.Err(); err != nil {
			log.Fatalf("Ошибка при чтении файла %s: %v", filename, err)
		}

		words := splitWords(text)
		result := make(map[string]bool)

		for _, word := range words {
			if len(word) > 2 {
				normalForm := getNormalForm(word)
				result[normalForm] = true
			}
		}

		return result
	}

	set1 := process("text_1.txt")
	set2 := process("text_2.txt")

	common := make(map[string]bool)
	for word := range set1 {
		if set2[word] {
			common[word] = true
		}
	}

	var similarity float64
	unionSize := len(set1) + len(set2) - len(common)
	if unionSize > 0 {
		similarity = float64(len(common)) / float64(unionSize) * 100
	}

	var commonSorted []string
	for word := range common {
		commonSorted = append(commonSorted, word)
	}
	sort.Strings(commonSorted)

	fmt.Println("\nЧасть 2: Сравнение текстов")
	fmt.Printf("Схожесть: %.1f%%\n", similarity)
	fmt.Printf("Совпадающие слова: %s\n", strings.Join(commonSorted, ", "))
}

func main() {
	part1()
	part2()
}
