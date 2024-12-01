#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <set>

using namespace std;

int part1() {
    ifstream f("day01/input.txt");
    
    int total = 0;
    
    string line;
    vector<int> nums1;
    vector<int> nums2;
    string delim = "   ";
    while (getline(f, line)) {
        string num1_str = line.substr(0, line.find(delim));
        string num2_str = line.substr(line.find(delim)+2,line.length());
        int num1, num2;
        num1 = stoi(num1_str);
        num2 = stoi(num2_str);
        nums1.push_back(num1);
        nums2.push_back(num2);
    }
    
    sort(nums1.begin(), nums1.end());
    sort(nums2.begin(), nums2.end());
    
    for (int i = 0; i < nums1.size(); i++) {
        total += abs(nums1[i]-nums2[i]);
    }
    
    return total;
}

int part2() {
    ifstream f("day01/input.txt");
    
    int total = 0;
    
    string line;
    set<int> nums1;
    vector<int> nums2;
    string delim = "   ";
    while (getline(f, line)) {
        string num1_str = line.substr(0, line.find(delim));
        // cout << num1 << endl;
        string num2_str = line.substr(line.find(delim)+2,line.length());
        int num1, num2;
        num1 = stoi(num1_str);
        num2 = stoi(num2_str);
        nums1.insert(num1);
        nums2.push_back(num2);
    }
    
    for (int n : nums1) {
        total += (n * count(nums2.begin(), nums2.end(), n));
    }
    return total;
}

int main() {
    cout << "Part 1: " << part1() << endl;
    cout << "Part 2: " << part2() << endl;
}
