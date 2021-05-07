"""Generate funny names by randomly combining names from 2 separate lists."""
import sys
import random

def main():
    """Choose names at random from 2 tuples of names and print to screen."""
    print("Welcome to the Psych 'Sidekick Name Picker.'\n")
    print("A name just like Sean would pick of Gus:\n\n")

    first = ('Dhamo', 'Raju', 'Raman', 'Baburao', 'Ganoo', 'Ghano', 'Gojo','Mansukh', 'Ramesh',
     'Hasmukh', 'Chinu', 'Ramnik', 'Goongo', 'Mahesh', 'Rakla', 'Geep', 'Dhansukh', 'Banto',
     'Huko', 'Vicky','Kaalu', 'Kaalo', 'Sambusa', 'Jinno', 'Upen', 'Bhupen', 'Mano', 'Lallulal',
     'Lalu', 'Lalo', 'Kallu', 'Jhand', 'Ghachar', 'Ganpat','Vakshay', 'Naresh', 'Naren', 'Nitin',
     'Kallu', 'Mallu', 'Bharat','Duryodhan', 'Nuro', 'Ashok', 'Wagmaru', 'Nimo', 'Dino', 'Banty',
     'Kano', 'Kaali', 'Hariyo', 'Babu', 'Chanu', 'Jhony', 'Kanu', 'Kanti')

    last = ('Gojo', 'Bhuro', 'Ghanti', 'Apte', 'Ghat', 'Jhand', 'Choido', 'land', 'langdo',
    'Dabal', 'Kaniyo', 'Bhut', 'Chor', 'Vandro','Jhanth', 'gaand', 'Sins', 'bhoot')

    while True:
        first_name = random.choice(first)
        last_name = random.choice(last)

        print("\n\n")
        print(f"{first_name} {last_name}.", file=sys.stderr)
        print("\n\n")

        try_again = input("\n\nTry Again ? (Continue : Enter, Quit : 'n')")
        if try_again.lower() == 'n':
            break

    input("\nPress Enter to exit.")

if __name__=="__main__":
    main()
