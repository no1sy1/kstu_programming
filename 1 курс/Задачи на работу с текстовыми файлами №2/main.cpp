#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
#include <regex>
#include <cmath>
#include <iomanip>

class MorphAnalyzer {
public:
    std::string getNormalForm(const std::string& word) {
        return word;
    }
};

std::vector<std::string> splitWords(const std::string& text) {
    std::regex non_alpha("[^а-яё\\s]");
    std::string cleaned = std::regex_replace(text, non_alpha, "");
    
    std::vector<std::string> words;
    std::regex word_regex("([а-яё]+)");
    auto words_begin = std::sregex_iterator(cleaned.begin(), cleaned.end(), word_regex);
    auto words_end = std::sregex_iterator();
    
    for (std::sregex_iterator i = words_begin; i != words_end; ++i) {
        words.push_back((*i).str());
    }
    
    return words;
}

void part1() {
    const std::unordered_set<std::string> STOP_WORDS = {"и", "в", "на", "с", "по"};
    MorphAnalyzer morph;
    
    std::ifstream file("text_1.txt");
    if (!file.is_open()) {
        std::cerr << "Не удалось открыть файл text_1.txt" << std::endl;
        return;
    }
    
    std::string text((std::istreambuf_iterator<char>(file)), 
                std::istreambuf_iterator<char>());
    file.close();
    
    std::transform(text.begin(), text.end(), text.begin(), 
                  [](unsigned char c){ return std::tolower(c); });
    
    auto words = splitWords(text);
    std::unordered_map<std::string, int> freq;
    
    for (const auto& word : words) {
        if (STOP_WORDS.find(word) != STOP_WORDS.end()) {
            continue;
        }
        
        std::string normal_form = morph.getNormalForm(word);
        freq[normal_form]++;
    }
    
    std::vector<std::pair<std::string, int>> sorted_words(freq.begin(), freq.end());
    std::sort(sorted_words.begin(), sorted_words.end(), 
             [](const auto& a, const auto& b) { return a.second > b.second; });
    
    int count = 0;
    for (const auto& [word, cnt] : sorted_words) {
        if (count++ >= 20) break;
        std::cout << word << ": " << cnt << std::endl;
    }
}

void part2() {
    MorphAnalyzer morph;
    
    auto process = [&morph](const std::string& text) {
        std::unordered_set<std::string> result;
        auto words = splitWords(text);
        
        for (const auto& word : words) {
            if (word.length() > 2) {
                result.insert(morph.getNormalForm(word));
            }
        }
        
        return result;
    };
    
    std::ifstream f1("text_1.txt"), f2("text_2.txt");
    if (!f1.is_open() || !f2.is_open()) {
        std::cerr << "Не удалось открыть один из файлов" << std::endl;
        return;
    }
    
    std::string text1((std::istreambuf_iterator<char>(f1)), 
                std::istreambuf_iterator<char>());
    std::string text2((std::istreambuf_iterator<char>(f2)), 
                std::istreambuf_iterator<char>());
    f1.close();
    f2.close();
    
    std::transform(text1.begin(), text1.end(), text1.begin(), 
                  [](unsigned char c){ return std::tolower(c); });
    std::transform(text2.begin(), text2.end(), text2.begin(), 
                  [](unsigned char c){ return std::tolower(c); });
    
    auto set1 = process(text1);
    auto set2 = process(text2);
    
    std::unordered_set<std::string> common;
    for (const auto& word : set1) {
        if (set2.find(word) != set2.end()) {
            common.insert(word);
        }
    }
    
    double similarity = 0.0;
    if (!set1.empty() || !set2.empty()) {
        size_t union_size = set1.size() + set2.size() - common.size();
        similarity = (common.size() * 100.0) / union_size;
    }
    
    std::cout << "Схожесть: " << std::fixed << std::setprecision(1) << similarity << "%" << std::endl;
    
    std::vector<std::string> common_sorted(common.begin(), common.end());
    std::sort(common_sorted.begin(), common_sorted.end());
    
    std::cout << "Совпадающие слова: ";
    for (size_t i = 0; i < common_sorted.size(); ++i) {
        if (i != 0) std::cout << ", ";
        std::cout << common_sorted[i];
    }
    std::cout << std::endl;
}

int main() {
    std::cout << "Часть 1: Частота слов\n";
    part1();
    
    std::cout << "\nЧасть 2: Сравнение текстов\n";
    part2();
    
    return 0;
}
