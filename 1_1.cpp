#include <iostream>

int gcd(int a, int b, int &x, int &y)
{
  if (a == 0)
  {
    x = 0;
    y = 1;
    return b;
  }

  int x1, y1;
  int d = gcd(b % a, a, x1, y1);
  std::cout << "x=" << x1 << " y=" << y1 << "\n";
  x = y1 - (b / a) * x1;
  y = x1;
  return d;
}

int main()
{
  int x, y;
  gcd(546, 212, x, y);
  std::cout << "x=" << x << " y=" << y << " " << 546 * x + 212 * y << "\n";
  return 0;
}