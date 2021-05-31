#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
using namespace std;

void TopoSort(int **a, int n)
{
    vector<int> indegree, queue; //mảng lưu bậc vào
    indegree.push_back(0);       //k tính đỉnh 0
    for (int j = 1; j < n; j++)
    {
        int tmp = 0;
        for (int i = 1; i < n; i++)
            tmp += a[i][j];
        indegree.push_back(tmp);
        if (tmp == 0) //cho những đỉnh có bậc vào = 0 vào queue
            queue.push_back(j);
    }

    while (!queue.empty())
    {
        int u = queue.front();
        queue.erase(queue.begin());
        cout << u << " ";
        for (int i = 1; i < n; i++)
            if (a[u][i] == 1)
            {
                if (--indegree[i] == 0)
                    queue.push_back(i);
            }
    }
    indegree.clear();
    queue.clear();
}

int main()
{
    fstream f;
    int n, **a;

    f.open("input1.txt", ios::in);
    f >> n;
    n = n + 1; //không tính chỉ số 0;
    a = new int *[n];
    for (int i = 0; i < n; i++)
    {
        a[i] = new int[n];
        for (int j = 0; j < n; j++)
            a[i][j] = 0;
    }
    string temp;
    getline(f, temp);
    while (temp != "0")
    {
        if (temp != "")
        {
            stringstream s(temp);
            int from, to;
            s >> to;
            while (s >> from)
                a[from][to] = 1;
        }
        getline(f, temp);
    }
    f.close();

    TopoSort(a, n);
    for (int i = 0; i < n; i++)
    {
        delete[] a[i];
        a[i] = nullptr;
    }
    delete[] a;
    a = nullptr;
    return 0;
}