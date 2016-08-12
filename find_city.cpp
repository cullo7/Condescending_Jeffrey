// reading a text file
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

/*
 * Function that parses a text file with two-letter country code and corresponding
 * names of countries. It then returns the full country name of the two-letter coutry
 * code entered.
 * 
 * Example line from country_mapping:
 *
 *    United States,US
 */

std::string get_country(std::string abbr){
  int n = 0;
  std::string line; // string object that will hold each line parsed
  int length = abbr.length();
  std::ifstream myfile ("country_mapping.txt"); // file containing country code mapping
  if (myfile.is_open())
  {
    while ( getline (myfile,line) )
    {
      for(int i = 0; i < line.length() && n < length ; i++){ //for loop exits when consecutive letters matched reaches the length of the search string
        if (line[i] == toupper(abbr[n])){
          n++;
        }
        else{
          n = 0;
        }
      }
      if (n == length){
        return line.substr(0,line.length()-3); // Return country name
      }
    }
    myfile.close();
  }
  else{ 
    std::cout << "Unable to open file";
  }
  return "no country found";
}

/*
 * Main method takes in a string that holds the name of a city
 * and subsequently searches worldcitiespop.txt to find the country code.
 * Finally get_country is called to retrieve the name of the country for
 * each instance.
 */
int main (int argc, char* argv[]) {

  std::string city = argv[1];

  // weed out cities containing sting, but possibly longer
  std::string search = ",";
  search.append(argv[1]);
  search.append(",");

  int length = search.length();
  std::string line;
  int n = 0; //variable to keep track of where in search string is found
  int comma = 0;

  std::vector<std::string> results; //vector to hold country codes found;
  std::vector<std::string> lats;
  std::vector<std::string> longs;
  std::ifstream myfile ("worldcitiespop.txt");
  
  std::string latitude = "";
  std::string longitude = "";

  bool word = false;

  if (myfile.is_open())
  {
    while ( getline (myfile,line) )
    {
      int i;
      for(i = 0; i < line.length(); i++){
        if(line[i] == ','){
          comma++;
        }
        else if(comma == 5 && word){
          latitude+=line[i];
        }
        else if(comma == 6 && word){
          longitude+=line[i];
        }
        if (line[i] == search[n]){
          n++;
          if(n == length){
            word = true;
          }
        }
        else{
          n = 0;
        }
     }
      comma = 0;
      if (word){
        results.push_back(line.substr(0,2));
        lats.push_back(latitude);
        longs.push_back(longitude);
        latitude = "";
        longitude = "";
        n = 0;
        word = false;
      }
    }
    myfile.close();
  }
  else {
    std::cout << "Unable to open file";
  }
  if(results.size() == 0){
    std::cout<<"No results found for that name ";
  }
  else{
    std::cout<<"City named "<<city<<" found in..."<<std::endl;
    for(int i = 0; i < results.size(); i++){
      std::cout<<i+1<<". "<<get_country(results.at(i))<<" Latitude: "<<lats.at(i)<<" Longitude "<<longs.at(i)<<std::endl;
    }
  }
  return 0;
}
