#ifndef CPP3_SMARTCALC_V_2_0_1_SRC_MODEL_H
#define CPP3_SMARTCALC_V_2_0_1_SRC_MODEL_H

#include <cmath>
#include <iostream>
#include <sstream>
#include <stack>
#include <string>

//#include <pybind11/pybind11.h>
//#include <Eigen/Dense>

//namespace s21 {
class Model {
 private:
  struct Data {
    char type_;  // 0 для чисел, знаки для операций
    double value_;  // 0 для операций, значение для чисел
  };
  double x_value_;

 public:
  Model(){};
  int finderrors(std::string& input_str);
  int isnumber(char c);
  int isnumber2(char c);
  int finderror_x(std::string& input_str);
  bool Calc(std::stack<Data>& Stack_chislo, std::stack<Data>& Stack_o,
            Data& item);
  int Priority(char operation);
  void Setter(double value);
  double Parsing(wchar_t* x, double value1);
  void Add(std::stack<Data>& Stack_chislo, std::stack<Data>& Stack_o,
           Data& item, double a);
  void Sub(std::stack<Data>& Stack_chislo, std::stack<Data>& Stack_o,
           Data& item, double a);
  void Mult(std::stack<Data>& Stack_chislo, std::stack<Data>& Stack_o,
            Data& item, double a);
  void Div(std::stack<Data>& Stack_chislo, std::stack<Data>& Stack_o,
           Data& item, double a);
  void Pow(std::stack<Data>& Stack_chislo, std::stack<Data>& Stack_o,
           Data& item, double a);
  void Mod(std::stack<Data>& Stack_chislo, std::stack<Data>& Stack_o,
           Data& item, double a);
  void Exp(std::stack<Data>& Stack_chislo, std::stack<Data>& Stack_o,
           Data& item, double a);
  void Sin(std::stack<Data>& Stack_chislo, std::stack<Data>& Stack_o,
           Data& item, double a);
  void Cos(std::stack<Data>& Stack_chislo, std::stack<Data>& Stack_o,
           Data& item, double a);
  void Tan(std::stack<Data>& Stack_chislo, std::stack<Data>& Stack_o,
           Data& item, double a);
  void Acos(std::stack<Data>& Stack_chislo, std::stack<Data>& Stack_o,
            Data& item, double a);
  void Asin(std::stack<Data>& Stack_chislo, std::stack<Data>& Stack_o,
            Data& item, double a);
  void Atan(std::stack<Data>& Stack_chislo, std::stack<Data>& Stack_o,
            Data& item, double a);
  void Ln(std::stack<Data>& Stack_chislo, std::stack<Data>& Stack_o, Data& item,
          double a);
  void Log(std::stack<Data>& Stack_chislo, std::stack<Data>& Stack_o,
           Data& item, double a);
  void Sqrt(std::stack<Data>& Stack_chislo, std::stack<Data>& Stack_o,
            Data& item, double a);
  void AnnuityCreditcalc(double summa, int period, double percent,
                         double& payment, double& totalpayment,
                         double& overpayment);
  void DiffCreditcalc(double summa, int period, double percent, double& payment,
                      double& totalpayment, double& overpayment,
                      double& summapercentMax, double& summapercentMin);

};
//}  // namespace s21

extern "C" {
    Model* Model_new(){ return new Model(); }
    int Model_parsing(Model* model, wchar_t* x, double value1){ return model->Parsing(x, value1); }
}

#endif  // CPP3_SMARTCALC_V_2_0_1_SRC_MODEL_H
