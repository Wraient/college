#include <iostream>

using namespace std;

class Complex {
  int real;
  int img;
  public:
    Complex(int r=0, int i=0){ 
      real = r;
      img = i;
    }
    Complex operator+(Complex const& obj)
    {
      Complex res;
      res.real = real + obj.real;
      res.img = img + obj.img;
      return res;
    }
    Complex operator*(Complex const& obj)
    {
      Complex res;
      res.real = real * obj.real;
      res.img = img * obj.img;
      return res;
    }
  /*  friend ostream & operator << (ostream &out, const Complex &c);*/
  /*  friend istream & operator << (istream &in, const Complex &c);*/
  /*};*/

    friend ostream &operator<<(ostream &out, const Complex &c)
    {
      out << c.real;
      out << " + " << c.img << "i" << endl;
      return out;
    }

    friend istream &operator<<(istream &in, const Complex &c)
    {
      cout << "Enter the real part ";
      in >> c.real;
      cout << "Enter the imaginary part ";
      in >> c.img;
      return in;
    }
    /*void print() { cout << real << " + " << img << "i" << "\n";}*/
};
int main(){
  Complex c1(5,5);
  Complex c2(2,2);
  Complex c3 = c1+c2;
  Complex c4 = c1*c2;
  /*cout << c3;*/
  /*c3.print(); */
  /*c4.print();*/
}

    /*friend istream &operator >> (ostream &input, Complex &t)*/
    /*{*/
    /*  cout << "Enter the real part: \n";*/
    /*  input>>t;*/
    /*  cout << "Enter the imaginary part: \n";*/
    /*  input>>t;*/
    /*}*/
    /*friend ostream &operator << (ostream &output, Complex &t)*/
    /*{*/
    /**/
    /*}*/
