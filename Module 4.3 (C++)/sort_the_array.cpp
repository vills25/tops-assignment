// Write a program of to sort the array using templates.

#include <iostream>
using namespace std;

template <typename T>
void bubbleSort(T arr[], int size)
{
    for (int i = 0; i < size - 1; ++i)
    {
        for (int j = 0; j < size - i - 1; ++j)
        {
            if (arr[j] > arr[j + 1])
            {
                // Swap arr[j] and arr[j + 1]
                T temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

template <typename T>
void printArray(T arr[], int size)
{
    for (int i = 0; i < size; ++i)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main()
{
    // Integer array
    int intArr[] = {5, 2, 8, 1, 9};
    int intSize = sizeof(intArr) / sizeof(intArr[0]);

    cout << "Before sorting (integer array): ";
    printArray(intArr, intSize);

    bubbleSort(intArr, intSize);

    cout << "After sorting (integer array): ";
    printArray(intArr, intSize);

    // Double array
    double doubleArr[] = {3.14, 1.23, 2.71, 0.99};
    int doubleSize = sizeof(doubleArr) / sizeof(doubleArr[0]);

    cout << "Before sorting (double array): ";
    printArray(doubleArr, doubleSize);

    bubbleSort(doubleArr, doubleSize);

    cout << "After sorting (double array): ";
    printArray(doubleArr, doubleSize);

    return 0;
}
