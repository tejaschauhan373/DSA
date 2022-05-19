#include<iostream>
#include<sstream>
#include<cstring>
#include<vector>
using namespace std;

vector<string> split(stringstream temp){
    vector<string> tokens;
    string token;
    while(getline(temp,token, ' ')){
        tokens.push_back(token);
    }
    return tokens;
}

int main(){
    //string input;
    //getline(cin, input);

    // create a string stream object
    //stringstream ss(input);

    //string token;

    //vector<string> tokens;

    //tokens = split(ss);

    char input[1000];
    cin.getline(input, 1000);

    //strtok()

    char *token = strtok(input, " ");

    while(token != NULL){
        cout << token;
        token = strtok(NULL, " ");
    }

    //for(auto token: tokens){
      //  cout << token <<", ";
    //}

    return 0;
}
