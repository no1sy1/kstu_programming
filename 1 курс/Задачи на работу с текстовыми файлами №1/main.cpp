#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    //1
    ifstream file("numbers.txt");
    double num, sum = 0;
    int count = 0;
    while (file >> num) {
        sum += num;
        count++;
    }
    file.close();
    double average = sum / count;
    cout << "Среднее арифметическое: " << average << endl;

    //2
    ifstream file("numbers.txt");
    double num, min, max;
    file >> num;
    min = max = num;
    while (file >> num) {
        if (num < min) min = num;
        if (num > max) max = num;
    }
    file.close();
    cout << "Min: " << min << "\nMax: " << max << endl;

    //3
    ifstream inputFile("numbers.txt");
    ofstream outputFile("even_numbers.txt");
    int number;
    while (inputFile >> number) {
        if (number % 2 == 0) {
            outputFile << number << ' ';
        }
    }

    //4
    ifstream file("text.txt"); 
    int lineCount = 0;
    string line;
    while (getline(file, line)) { 
        lineCount++;  
    }
    cout << "Количество строк: " << lineCount << endl;

    //5
    ifstream file("My_text.txt");  
    int wordCount = 0;
    string word;
    while (file >> word) {
        wordCount++;
    }
    cout << "Количество слов: " << wordCount << endl;

    //6
    string filename = "text.txt";
    string old_word, new_word;

    cout << "Введите слово для замены: ";
    getline(cin, old_word);
    cout << "Введите новое слово: ";
    getline(cin, new_word);
    ifstream inFile(filename);
    string content((istreambuf_iterator<char>(inFile)), {});
    inFile.close();
    size_t pos = 0;
    while ((pos = content.find(old_word, pos)) != string::npos) {
        content.replace(pos, old_word.length(), new_word);
        pos += new_word.length();
    }
    ofstream outFile(filename);
    outFile << content;
    outFile.close();

    return 0;
}
