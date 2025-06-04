//1
#include <iostream>
#include <fstream>

using namespace std;

int main() {
    ifstream in("input.cpp");
    ofstream out("output.txt");
    
    int balance = 0;
    char k;
    
    while (in.get(k)) {
        if (k == '{') {
            balance++;
        }
        else if (k == '}') {
            balance--;
            if (balance < 0) {
                balance = 0;
            }
        }
    }

    if (balance > 0) {
        cout << "Фигурные скобки не закрыты" << endl;
        out << "Фигурные скобки не закрыты" << endl;
    }
    else if (balance == 0) {
        cout << "Все фигурные скобки закрыты" << endl;
        out << "Все фигурные скобки закрыты" << endl;
    }

    in.close();
    out.close();
    return 0;
}
