#include "model.h"


int Model::isnumber(char c) {
  return ((c >= '0' && c <= '9') || c == '.' || c == 'x');
}
int Model::isnumber2(char c) {
  return ((c >= '0' && c <= '9') || c == 'x');
}
int Model::finderrors(std::string& input_str) {
  int flag = 0;
  int i = 0, leftb = 0, rightb = 0;
  for (i = 0; input_str[i] != '\0'; i++) {
    if (input_str[i] == '(') {
      leftb++;
    } else if (input_str[i] == ')') {
      rightb++;
      if (rightb > leftb) flag = 1;
    }
    if (input_str[i] == '(' &&
        (input_str[i + 1] == '*' || input_str[i + 1] == '/' ||
         input_str[i + 1] == '^' || input_str[i + 1] == '%'))
      flag = 1;
    if (input_str[i] == '/' && input_str[i + 1] == '0') flag = 1;
    if ((input_str[i] == '*' || input_str[i] == '/' || input_str[i] == '^' ||
         input_str[i] == '%') &&
        !isnumber(input_str[i - 1])) {
      if (input_str[i - 1] != ')') flag = 1;
    }
    if ((input_str[i] == '*' || input_str[i] == '/' || input_str[i] == '^' ||
         input_str[i] == '%' || input_str[i] == '+' || input_str[i] == '-') &&
        !isnumber(input_str[i + 1])) {
      if (input_str[i + 1] != '(') {
        if (input_str[i + 1] == 'c' || input_str[i + 1] == 's' ||
            input_str[i + 1] == 't' || input_str[i + 1] == 'a' ||
            input_str[i + 1] == 'l') {
          flag = 0;
        } else
          flag = 1;
      }
    }
    if (input_str[i] == '.' && !isnumber2(input_str[i + 1])) flag = 1;
    if (input_str[i] == 'x' && (isnumber(input_str[i + 1]) || isnumber(input_str[i - 1]))) flag = 1;
  }
  if (leftb != rightb) flag = 1;
  return flag;
}

int Model::finderror_x(std::string& input_str) {
  int flag = 0;
  int i = 0;
  int j = 0;
  int k = 0;
  for (i = 0; input_str[i] != '\0'; ++i) {
    if (input_str[i] == '.') ++j;
    if (input_str[i] == '-') ++k;
    if (input_str[i] == '-' && !isnumber(input_str[i + 1])) flag = 1;
  }
  if (j > 1 || k > 1) flag = 1;
  return flag;
}
double Model::Parsing(wchar_t* x, double value1) {
  std::wstring ws(x);
  std::string str(ws.begin(), ws.end());
  double result = 0;
  double status = 0;
  if (finderrors(str) == 1) {
//    std::cout << "error" << std::endl;
    status = 2024.20242024;
    return status;
  } else {
    std::stringstream sstr{str};
    char operation;
    bool flag = 1;
    std::stack<Data> Stack_chislo;  //Стек с числами
    std::stack<Data> Stack_o;       //Стек с операциями
    Data item;                      // объект структуры
    while (sstr) {
      operation = sstr.peek();
      if (operation == '\377')
        break;  //Если достигнут конец строки, выходим из цикла
      if (operation == ' ') {  //Игнорирование пробелов
        sstr.ignore();
        continue;
      }
      if (operation == 'c' || operation == 't') {
        char foo[3];
        for (int i = 0; i < 3; i++) {
          operation = sstr.peek();
          foo[i] = operation;
          sstr.ignore();
        }

        if (foo[0] == 'c' && foo[1] == 'o' && foo[2] == 's') {
          item.type_ = 'c';
          item.value_ = 0;
          Stack_o.push(item);
          continue;
        }
        if (foo[0] == 't' && foo[1] == 'a' && foo[2] == 'n') {
          item.type_ = 't';
          item.value_ = 0;
          Stack_o.push(item);
          continue;
        }
      }
      if (operation == 's') {
        char foo[3];
        char foo2[4];
        for (int i = 0; i < 3; i++) {
          operation = sstr.peek();
          foo[i] = operation;
          sstr.ignore();
        }
        if (foo[0] == 's' && foo[1] == 'i' && foo[2] == 'n') {
          item.type_ = 's';
          item.value_ = 0;
          Stack_o.push(item);
          continue;
        } else if (foo[0] == 's' && foo[1] == 'q' && foo[2] == 'r') {
          for (int j = 0; j < 4; j++) {
            foo2[j] = foo[j];
          }
          operation = sstr.peek();
          foo2[3] = operation;
          sstr.ignore();

          if (foo2[0] == 's' && foo2[1] == 'q' && foo2[2] == 'r' &&
              foo2[3] == 't') {
            item.type_ = 'q';
            item.value_ = 0;
            Stack_o.push(item);
            continue;
          }
        }
      }
      if (operation == 'l') {
        char foo[2];
        char foo2[3];
        for (int i = 0; i < 2; i++) {
          operation = sstr.peek();
          foo[i] = operation;
          sstr.ignore();
        }
        if (foo[0] == 'l' && foo[1] == 'n') {
          item.type_ = 'n';
          item.value_ = 0;
          Stack_o.push(item);
          continue;
        } else if (foo[0] == 'l' && foo[1] == 'o') {
          for (int j = 0; j < 3; j++) {
            foo2[j] = foo[j];
          }
          operation = sstr.peek();
          foo2[2] = operation;
          sstr.ignore();

          if (foo2[0] == 'l' && foo2[1] == 'o' && foo2[2] == 'g') {
            item.type_ = 'l';
            item.value_ = 0;
            Stack_o.push(item);
            continue;
          }
        }
      }
      if (operation == 'a') {
        char foo[4];
        for (int i = 0; i < 4; i++) {
          operation = sstr.peek();
          foo[i] = operation;
          sstr.ignore();
        }
        if (foo[0] == 'a' && foo[1] == 's' && foo[2] == 'i' && foo[3] == 'n') {
          item.type_ = 'i';
          item.value_ = 0;
          Stack_o.push(item);
          continue;
        }
        if (foo[0] == 'a' && foo[1] == 'c' && foo[2] == 'o' && foo[3] == 's') {
          item.type_ = 'o';
          item.value_ = 0;
          Stack_o.push(item);
          continue;
        }
        if (foo[0] == 'a' && foo[1] == 't' && foo[2] == 'a' && foo[3] == 'n') {
          item.type_ = 'g';
          item.value_ = 0;
          Stack_o.push(item);
          continue;
        }
      }
      if (operation == 'E') {
        item.type_ = 'E';
        item.value_ = 0;
        Stack_o.push(item);
        sstr.ignore();
        continue;
      }
      if ((operation >= '0' && operation <= '9') ||
          (operation == '-' && flag == 1)) {
        double value;
        sstr >> value;
        item.type_ = '0';
        item.value_ = value;
        Stack_chislo.push(item);
        flag = 0;
        continue;
      }
      if (operation == 'x') {
        item.type_ = '0';
//        item.value_ = x_value_;
        item.value_ = value1;
        Stack_chislo.push(item);
        flag = 0;
        sstr.ignore();
        continue;
      }

      if (operation == '+' || (operation == '-' && flag == 0) ||
          operation == '*' || operation == '/' || operation == '^' ||
          operation == '%') {
        if (Stack_o.size() == 0) {  //Если стек с операциями пуст
          item.type_ = operation;
          item.value_ = 0;
          Stack_o.push(item);
          sstr.ignore();
          continue;
        }
        if (Stack_o.size() != 0 &&
            Priority(operation) >
                Priority(
                    Stack_o.top().type_)) {  //Если стек с операциями НЕ пуст,
                                             //но приоритет текущей операции
                                             //выше верхней в стеке с операциями
          item.type_ = operation;
          item.value_ = 0;
          Stack_o.push(item);
          sstr.ignore();
          continue;
        }
        if (Stack_o.size() != 0 &&
            Priority(operation) <=
                Priority(Stack_o.top()
                             .type_)) {  //Если стек с операциями НЕ пуст, но
                                         //приоритет текущей операции ниже либо
                                         //равен верхней в стеке с операциями
          Calc(Stack_chislo, Stack_o, item);
        }
      }
      if (operation == '(') {
        item.type_ = operation;
        item.value_ = 0;
        Stack_o.push(item);
        sstr.ignore();
        flag = 1;
        continue;
      }
      if (operation == ')') {
        while (Stack_o.top().type_ != '(') {
          Calc(Stack_chislo, Stack_o, item);
        }
        Stack_o.pop();
        sstr.ignore();
        continue;
      }
    }
    while (Stack_o.size() != 0) {
      Calc(Stack_chislo, Stack_o, item);
    }
    result = Stack_chislo.top().value_;
  }
//   std::cout << result << std::endl;
//  return status;
    return result;
}

int Model::Priority(char operation) {
  if (operation == 's' || operation == 'c' || operation == 't' ||
      operation == 'g' || operation == 'E' || operation == 'l' ||
      operation == 'n')
    return 4;
  if (operation == '^') return 3;
  if (operation == '*' || operation == '/' || operation == '%') return 2;
  if (operation == '+' || operation == '-')
    return 1;
  else
    return 0;
}

void Model::Setter(double value) {
  x_value_ = value;
  }

bool Model::Calc(std::stack<Data>& Stack_chislo, std::stack<Data>& Stack_o,
                      Data& item) {
  double a;
  a = Stack_chislo.top().value_;
  Stack_chislo.pop();
  switch (Stack_o.top().type_) {
    case '+':
      Add(Stack_chislo, Stack_o, item, a);
      break;
    case '-':
      Sub(Stack_chislo, Stack_o, item, a);
      break;
    case '^':
      Pow(Stack_chislo, Stack_o, item, a);
      break;
    case '%':
      Mod(Stack_chislo, Stack_o, item, a);
      break;
    case '*':
      Mult(Stack_chislo, Stack_o, item, a);
      break;
    case '/':
      if (a == 0) {
        return false;
      } else {
        Div(Stack_chislo, Stack_o, item, a);
        break;
      }
    case 's':
      Sin(Stack_chislo, Stack_o, item, a);
      break;
    case 'c':
      Cos(Stack_chislo, Stack_o, item, a);
      break;
    case 't':
      Tan(Stack_chislo, Stack_o, item, a);
      break;
    case 'o':
      Acos(Stack_chislo, Stack_o, item, a);
      break;
    case 'i':
      Asin(Stack_chislo, Stack_o, item, a);
      break;
    case 'g':
      Atan(Stack_chislo, Stack_o, item, a);
      break;
    case 'q':
      Sqrt(Stack_chislo, Stack_o, item, a);
      break;
    case 'l':
      Log(Stack_chislo, Stack_o, item, a);
      break;
    case 'n':
      Ln(Stack_chislo, Stack_o, item, a);
      break;
    case 'E':
      Exp(Stack_chislo, Stack_o, item, a);
      break;
    default:
      std::cerr << "\nError!\n";
      return false;
      break;
  }
  return true;
}

void Model::Add(std::stack<Data>& Stack_chislo, std::stack<Data>& Stack_o,
                     Data& item, double a) {
  double b, c;
  b = Stack_chislo.top().value_;
  Stack_chislo.pop();
  c = a + b;
  item.type_ = '0';
  item.value_ = c;
  Stack_chislo.push(item);
  Stack_o.pop();
}
void Model::Sub(std::stack<Data>& Stack_chislo, std::stack<Data>& Stack_o,
                     Data& item, double a) {
  double b, c;
  b = Stack_chislo.top().value_;
  Stack_chislo.pop();
  c = b - a;
  item.type_ = '0';
  item.value_ = c;
  Stack_chislo.push(item);
  Stack_o.pop();
}
void Model::Mult(std::stack<Data>& Stack_chislo, std::stack<Data>& Stack_o,
                      Data& item, double a) {
  double b, c;
  b = Stack_chislo.top().value_;
  Stack_chislo.pop();
  c = a * b;
  item.type_ = '0';
  item.value_ = c;
  Stack_chislo.push(item);
  Stack_o.pop();
}

void Model::Div(std::stack<Data>& Stack_chislo, std::stack<Data>& Stack_o,
                     Data& item, double a) {
  double b, c;
  b = Stack_chislo.top().value_;
  if (a != 0) {
    Stack_chislo.pop();
    c = (b / a);
    item.type_ = '0';
    item.value_ = c;
    Stack_chislo.push(item);
    Stack_o.pop();
  }
}
void Model::Pow(std::stack<Data>& Stack_chislo, std::stack<Data>& Stack_o,
                     Data& item, double a) {
  double b, c;
  b = Stack_chislo.top().value_;
  Stack_chislo.pop();
  c = pow(b, a);
  item.type_ = '0';
  item.value_ = c;
  Stack_chislo.push(item);
  Stack_o.pop();
}
void Model::Mod(std::stack<Data>& Stack_chislo, std::stack<Data>& Stack_o,
                     Data& item, double a) {
  double b, c;
  b = Stack_chislo.top().value_;
  Stack_chislo.pop();
  c = fmod(b, a);
  item.type_ = '0';
  item.value_ = c;
  Stack_chislo.push(item);
  Stack_o.pop();
}
void Model::Exp(std::stack<Data>& Stack_chislo, std::stack<Data>& Stack_o,
                     Data& item, double a) {
  double b, c;
  b = Stack_chislo.top().value_;
  Stack_chislo.pop();
  c = a * std::pow(10, b);
  item.type_ = '0';
  item.value_ = c;
  Stack_chislo.push(item);
  Stack_o.pop();
}
void Model::Sin(std::stack<Data>& Stack_chislo, std::stack<Data>& Stack_o,
                     Data& item, double a) {
  double c;
  c = std::sin(a);
  item.type_ = '0';
  item.value_ = c;
  Stack_chislo.push(item);
  Stack_o.pop();
}
void Model::Cos(std::stack<Data>& Stack_chislo, std::stack<Data>& Stack_o,
                     Data& item, double a) {
  double c;
  c = std::cos(a);
  item.type_ = '0';
  item.value_ = c;
  Stack_chislo.push(item);
  Stack_o.pop();
}
void Model::Tan(std::stack<Data>& Stack_chislo, std::stack<Data>& Stack_o,
                     Data& item, double a) {
  double c;
  c = std::tan(a);
  item.type_ = '0';
  item.value_ = c;
  Stack_chislo.push(item);
  Stack_o.pop();
}
void Model::Acos(std::stack<Data>& Stack_chislo, std::stack<Data>& Stack_o,
                      Data& item, double a) {
  double c;
  c = std::acos(a);
  item.type_ = '0';
  item.value_ = c;
  Stack_chislo.push(item);
  Stack_o.pop();
}
void Model::Asin(std::stack<Data>& Stack_chislo, std::stack<Data>& Stack_o,
                      Data& item, double a) {
  double c;
  c = std::asin(a);
  item.type_ = '0';
  item.value_ = c;
  Stack_chislo.push(item);
  Stack_o.pop();
}
void Model::Atan(std::stack<Data>& Stack_chislo, std::stack<Data>& Stack_o,
                      Data& item, double a) {
  double c;
  c = std::atan(a);
  item.type_ = '0';
  item.value_ = c;
  Stack_chislo.push(item);
  Stack_o.pop();
}
void Model::Ln(std::stack<Data>& Stack_chislo, std::stack<Data>& Stack_o,
                    Data& item, double a) {
  double c;
  c = std::log(a);
  item.type_ = '0';
  item.value_ = c;
  Stack_chislo.push(item);
  Stack_o.pop();
}
void Model::Log(std::stack<Data>& Stack_chislo, std::stack<Data>& Stack_o,
                     Data& item, double a) {
  double c;
  c = std::log10(a);
  item.type_ = '0';
  item.value_ = c;
  Stack_chislo.push(item);
  Stack_o.pop();
}
void Model::Sqrt(std::stack<Data>& Stack_chislo, std::stack<Data>& Stack_o,
                      Data& item, double a) {
  double c;
  c = std::sqrt(a);
  item.type_ = '0';
  item.value_ = c;
  Stack_chislo.push(item);
  Stack_o.pop();
}
// type annuity
void Model::AnnuityCreditcalc(double summa, int period, double percent,
                                   double& payment, double& totalpayment,
                                   double& overpayment) {
  double index = percent / (double)1200;
  double annIndex = index * pow((1 + index), (double)period) /
                    (pow((1 + index), (double)period) - 1);
  payment = annIndex * summa;
  totalpayment = payment * (double)period;
  overpayment = totalpayment - summa;
}

// type differentiated
void Model::DiffCreditcalc(double summa, int period, double percent,
                                double& payment, double& totalpayment,
                                double& overpayment, double& summapercentMax,
                                double& summapercentMin) {
  double pay = summa / (double)period;  //платеж по основному долгу
  double percentMax = (summa * percent / 100 * 30.4) /
                      365.25;  //сумма начисленных процентов в месяц max
  double percentMin = (pay * percent / 100 * 30.4) /
                      365.25;  //сумма начисленных процентов в месяц min
  double summapercent = (percentMax + percentMin) / 2;
  summapercentMax = pay + percentMax;
  summapercentMin = pay + percentMin;
  payment = pay + summapercent;
  totalpayment = payment * (double)period;
  overpayment = totalpayment - summa;
}
