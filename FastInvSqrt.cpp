#include <iostream>
#include<time.h>

float FastInvSqrt(float x) { // 求更好x的倒数
    float xhalf = 0.5f * x;
    int i = *(int *) &x;         // evil floating point bit level hacking
    i = 0x5f375a86 - (i >> 1);  // what the fuck?
    x = *(float *) &i;
    x = x * (1.5f - (xhalf * x * x));
    return x;
}

int main() {
    clock_t start, finish;
    double totaltime;
    start = clock();
    float b = FastInvSqrt(10);
    finish = clock();
    totaltime = (double) (finish - start) / CLOCKS_PER_SEC;
    std::cout << "\n此程序的运行时间为" << totaltime << "秒！" << std::endl;

    std::cout << b << std::endl;
    return 0;
}