#include <algorithm>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include "../common/utils.cpp"

using namespace std;

bool rev_comp(int a, int b) {
    return a >= b;
}

bool is_safe(vector<int> nums) {
    vector<int> diffs;
    for (int i = 0; i < nums.size()-1; i++) {
        int n1 = nums[i];
        int n2 = nums[i+1];
        diffs.push_back(abs(n1-n2));
    }
    int safeties = count(diffs.begin(), diffs.end(), 1) +
        count(diffs.begin(), diffs.end(), 2) +
        count(diffs.begin(), diffs.end(), 3);

    vector<int> sort1(nums);
    vector<int> sort2(nums);
    sort(sort1.begin(), sort1.end(), rev_comp);
    sort(sort2.begin(), sort2.end());

    return (safeties == diffs.size()) && ((sort1 == nums) || (sort2 == nums));
}

int part1() {
    ifstream f("day02/input.txt");

    string line;
    int total = 0;
    while (getline(f, line)) {
        vector<int> nums;
        for (string s : split(line, " ")) {
            int n = stoi(s);
            nums.push_back(n);
        }

        if (is_safe(nums)) {
            total++;
        }
    }

    return total;
}

int part2() {
    ifstream f("day02/input.txt");

    string line;
    int total = 0;
    while (getline(f, line)) {
        vector<int> nums;
        for (string s : split(line, " ")) {
            int n = stoi(s);
            nums.push_back(n);
        }

        for (int n : nums) {
            vector<int> nums_copy(nums);
            nums_copy.erase(find(nums_copy.begin(), nums_copy.end(), n));

            if (is_safe(nums_copy)) {
                total++;
                break;
            }
        }
    }

    return total;
}

int main() {
    cout << "Part 1: " << part1() << endl;
    cout << "Part 2: " << part2() << endl;
}
