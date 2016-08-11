// reading a text file
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

string get_country(string abbr){
  int n = 0;
  string line;
  int length = abbr.length();
  ifstream myfile ("country_mapping.txt");
  if (myfile.is_open())
  {
    while ( getline (myfile,line) )
    {
      for(int i = 0; i < line.length() && n < length ; i++){
        if (line[i] == toupper(abbr[n])){
          n++;
        }
        else{
          n = 0;
        }
      }
      if (n == length){
        myfile.close();
        return line.substr(0,line.length()-3);
      }
    }
    myfile.close();
  }
  return "no country found";
}

int main (int argc, char* argv[]) {
  string city = argv[1];
  cout<<city<<endl;
  int length = strlen(argv[1]);
  cout<<length<<endl;
  string line;
  int n = 0;
  vector<string> results;
  ifstream myfile ("worldcitiespop.txt");
  if (myfile.is_open())
  {
    while ( getline (myfile,line) )
    {
      int i;
      for(i = 0; i < line.length() && n < length; i++){
        if (line[i] == city[n]){
          n++;
        }
        else{
          n = 0;
        }
      }
      if (n == length){
        cout<<"pushed"<<line.substr(i-n,n)<<endl;
        results.push_back(line.substr(0,2));
      }
    }
    myfile.close();
  }
  else {
    cout << "Unable to open file";
  }
  for(int i = 0; i < results.size(); i++){
    cout<<i<<". "<<get_country(results.back())<<endl;
    results.pop_back();
  }

  return 0;
}
