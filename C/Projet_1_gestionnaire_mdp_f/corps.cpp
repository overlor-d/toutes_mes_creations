#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdlib>

void clearScreen() {
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif
}

using namespace std;

// Définition de la structure pour stocker les informations de mot de passe
struct PasswordInfo {
    string name;
    string username;
    string password;
};

// Fonction pour afficher les informations de mot de passe
void displayPasswordInfo(const PasswordInfo& passwordInfo) {
    cout << "Name: " << passwordInfo.name << endl;
    cout << "Username: " << passwordInfo.username << endl;
    cout << "Password: " << passwordInfo.password << endl << endl;
}

// Fonction pour ajouter un nouveau mot de passe
void addPassword(vector<PasswordInfo>& passwordList) {
    PasswordInfo passwordInfo;
    clearScreen();

    cout << "Enter name: ";
    cin >> passwordInfo.name;

    cout << "Enter username: ";
    cin >> passwordInfo.username;

    cout << "Enter password: ";
    cin >> passwordInfo.password;

    passwordList.push_back(passwordInfo);
}

// Fonction pour afficher tous les mots de passe
void displayAllPasswords(const vector<PasswordInfo>& passwordList) {
    clearScreen();
    cout << "Password List:\n1. Quitter\n" << endl;
    cout << "*------------------------------------------------*" << endl;
    for (const auto& passwordInfo : passwordList) {
        displayPasswordInfo(passwordInfo);
        cout << "==*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-==\n" << endl;
    }
    cout << "Choisissez : ";
    int choice;
    cin >> choice;
    switch (choice) {
        case 1:
            break;
    }

}

// Fonction pour enregistrer les mots de passe dans un fichier
void savePasswords(const vector<PasswordInfo>& passwordList) {
    ofstream outFile("Fichiers/passwords.txt");
    clearScreen();

    for (const auto& passwordInfo : passwordList) {
        outFile << passwordInfo.name << " "
                << passwordInfo.username << " "
                << passwordInfo.password << endl;
    }

    outFile.close();

    cout << "Passwords saved successfully." << endl;
}

// Fonction pour charger les mots de passe à partir d'un fichier
void loadPasswords(vector<PasswordInfo>& passwordList) {
    ifstream inFile("Fichiers/passwords.txt");
    clearScreen();

    PasswordInfo passwordInfo;
    while (inFile >> passwordInfo.name >> passwordInfo.username >> passwordInfo.password) {
        passwordList.push_back(passwordInfo);
    }

    inFile.close();

    cout << "Passwords loaded successfully." << endl;
}

int main() {
    vector<PasswordInfo> passwordList;

    // Charger les mots de passe à partir du fichier
    loadPasswords(passwordList);

    // Boucle principale du programme
    while (true) {
        clearScreen();


        cout << "--------- Gestionnaire de mot de passe ---------" << endl;
        cout << "1. Ajouter mdp" << endl;
        cout << "2. Afficher les mdp" << endl;
        cout << "3. Sauvegarder les mdp" << endl;
        cout << "4. Quitter" << endl;
        cout << "Choisissez : ";

        int choice;
        cin >> choice;

        switch (choice) {
            case 1:
                addPassword(passwordList);
                break;
            case 2:
                displayAllPasswords(passwordList);
                break;
            case 3:
                savePasswords(passwordList);
                break;
            case 4:
                // Quitter le programme
                return 0;
            default:
                cout << "Invalid choice." << endl;
        }
    }

    return 0;
}