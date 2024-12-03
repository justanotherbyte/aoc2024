#include <iostream>
#include <fstream>
#include <string>
#include <regex>

using namespace std;

int prod_mul(string s) {
    const regex pattern("\\d+");
    sregex_iterator iter = sregex_iterator(s.begin(), s.end(), pattern);
    sregex_iterator end = sregex_iterator();

    vector<int> nums;

    for (auto i = iter; i != end; i++) {
        nums.push_back(stoi(i->str()));
    }

    return (nums[0] * nums[1]);
}

int part1() {
    ifstream f("day03/input.txt");
    string text;

    string line;
    while (getline(f, line)) {
        text.append(line);
    }

    const regex mul_reg("mul\\(\\d+,\\d+\\)");

    sregex_iterator iter = sregex_iterator(text.begin(), text.end(), mul_reg);
    sregex_iterator iter_end = sregex_iterator();

    int total = 0;
    for (auto i = iter; i != iter_end; i++) {
        total += prod_mul(i->str());
    }

    return total;
}

int part2() {
    ifstream f("day03/input.txt");
    string text;

    string line;
    while (getline(f, line)) {
        text.append(line);
    }

    const regex reg("mul\\((\\d+),(\\d+)\\)|(don't\\(\\))|(do\\(\\))");

    sregex_iterator iter = sregex_iterator(text.begin(), text.end(), reg);
    sregex_iterator end = sregex_iterator();

    int total = 0;
    bool compute = true;
    for (auto m = iter; m != end; m++) {
        string match = m->str();
        if ((match == "don't()") || (match == "do()")) {
            compute = (match == "do()");
            continue;
        }

        if (compute) {
            total += prod_mul(match);
        }
    }

    return total;
}

int main() {
    cout << "Part 1: " << part1() << endl;
    cout << "Part 2: " << part2() << endl;
}
