#include <vector>

class Solution {
public:
    void setZeroes(std::vector<std::vector<int>>& matrix) {
        std::vector<int> a;
        std::vector<int> b;

        int m = matrix.size();
        int n = matrix[0].size();

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (matrix[i][j] == 0) {
                    a.push_back(i);
                    b.push_back(j);
                }
            }
        }

        for (int x : a) {
            for (int j = 0; j < n; ++j) {
                matrix[x][j] = 0;
            }
        }

        for (int y : b) {
            for (int k = 0; k < m; ++k) {
                matrix[k][y] = 0;
            }
        }
    }
};