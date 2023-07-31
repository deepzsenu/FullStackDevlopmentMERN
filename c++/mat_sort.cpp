#include <iostream>
#include <vector>
using namespace std;

int getRowSum(vector<int>& row) {
    int sum = 0;
    for (int num : row) {
        sum += num;
    }
    return sum;
}

void bubbleSortRows(vector<vector<int>>& matrix) {
    int numRows = matrix.size();
    for (int i = 0; i < numRows - 1; i++) {
        for (int j = 0; j < numRows - i - 1; j++) {
            int currRowSum = getRowSum(matrix[j]);
            int nextRowSum = getRowSum(matrix[j + 1]);
            if (currRowSum > nextRowSum) {
                swap(matrix[j], matrix[j + 1]);
            }
        }
    }
}

void printMatrix(const vector<vector<int>>& matrix) {
    for (const auto& row : matrix) {
        for (int num : row) {
            cout << num << " ";
        }
        cout << endl;
    }
}

int main() {
    vector<vector<int>> matrix = {{5, 2, 8}, {1, 6, 9}, {3, 4, 7}};

    cout << "Original Matrix:" << endl;
    printMatrix(matrix);

    bubbleSortRows(matrix);

    cout << "\nSorted Matrix:" << endl;
    printMatrix(matrix);

    return 0;
}
