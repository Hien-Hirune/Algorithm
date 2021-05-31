#include <iostream>
#include <fstream>

using namespace std;

int Selection(float *a, int left, int right, float k)
{
    if (left == right) //nếu k tìm thấy thì return -1
        return -1;
    int x = left + ((k-a[left])*(right-left)/(a[right]+a[left]));
    if (a[x] == k)
        return x;
    if (a[x] > k)
        return Selection(a, left, x - 1, k);
    else
        return Selection(a, x + 1, right, k);
}

//Nếu không tìm thấy thì return -1
int main()
{
    fstream f;
    int n;
    float *a, k;
    f.open("input4.txt", ios::in);
    f >> n;
    a = new float[n];
    for (int i = 0; i < n; i++)
        f >> a[i];
    f >> k;
    f.close();

    int pos = Selection(a,0,n-1,k);
    cout << pos << endl;
    delete[] a;
    a = nullptr;
    return 0;
}