#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <ctime>
#include <time.h>
#include <iomanip>
#include <cstring>

using namespace std;

void clearScreen() {
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif
}

struct Event {
    string name;
    string date;
};

void addEvent(vector<Event>& eventList) {
    clearScreen();

    string eventName;
    string eventDate;
    cout << "Entrez le nom de l'evenement: ";
    cin >> eventName;
    cout << "Entrez la date de l'evenement (AAAA-MM-JJ) : ";
    cin >> eventDate;

    bool eventFound = false;
    for (auto& event : eventList) {
        if (event.date == eventDate) {
            event.name += " | " + eventName;
            eventFound = true;
            break;
        }
    }

    if (!eventFound) {
        Event event = {eventName, eventDate};
        eventList.push_back(event);
    }
}

void displayAllEvents(const vector<Event>& eventList) {
    clearScreen();
    cout << "Liste des evenements:" << endl;
    for (const auto& event : eventList) {
        cout << event.date << ": " << event.name << endl;
    }
    cout << endl;
}

void saveEvents(const vector<Event>& eventList) {
    ofstream outFile("Fichiers/events.txt");
    clearScreen();

    for (const auto& event : eventList) {
        outFile << event.date << " " << event.name << endl;
    }

    outFile.close();

    cout << "evenements sauvegardes avec succes." << endl;
}

void loadEvents(vector<Event>& eventList) {
    ifstream inFile("Fichiers/events.txt");
    clearScreen();

    string eventName;
    string eventDate;
    while (inFile >> eventDate >> eventName) {
        Event event = {eventName, eventDate};
        eventList.push_back(event);
    }

    inFile.close();

    cout << "evenements charges avec succes." << endl;
}



int main() {
    vector<Event> eventList;

    loadEvents(eventList);

    while (true) {
        clearScreen();
        cout << "Que voulez-vous faire ?" << endl;
        cout << "1 - Ajouter un evenement" << endl;
        cout << "2 - Afficher tous les evenements" << endl;
        cout << "3 - Sauvegarder les evenements" << endl;
        cout << "4 - Quitter" << endl;
        int choice;
        cin >> choice;

        switch (choice) {
            case 1:
                addEvent(eventList);
                break;
            case 2:
                displayAllEvents(eventList);
                break;
            case 3:
                saveEvents(eventList);
                break;
            case 4:
                return 0;
            default:
                cout << "Entree invalide." << endl;
                break;
        }

        cout << "Appuyez sur Entrée pour continuer...";
        cin.ignore();
        cin.get();
    }

    return 0;
}
