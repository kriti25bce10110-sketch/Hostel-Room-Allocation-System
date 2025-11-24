students = []
rooms = {
    "B1": "free", "B2": "free", "B3": "free",    # Boys hostel rooms
    "G1": "free", "G2": "free", "G3": "free"     # Girls hostel rooms
}

allocated = {}  

while True:
    print("===== HOSTEL ROOM ALLOCATION SYSTEM =====")
    print("1. Register Student")
    print("2. Allocate Room")
    print("3. View Reports")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # 1. Register a new student
    if choice == "1":
        name = input("Enter student name: ")
        roll_num = input("Enter roll number: ")
        gender = input("Enter gender (M/F): ")

        # Check if already registered
        already = False
        for s in students:
            if s["roll"] == roll:
                already = True

        if already:
            print("Student already registered.")
        else:
            students.append({"name": name, "roll": roll_num, "gender": gender})
            print("Student registered successfully!")

    # 2. Allocate room
    elif choice == "2":
        roll_num = input("Enter roll number: ")

        # Check if student exists
        std = None
        for s in students:
            if s["roll"] == roll_num:
                std = s

        if std is None:
            print("Student not found. Register first.")
        else:
            # Check if already allotted
            if roll_num in allocated:
                print("Room already allocated:", allocated[roll_num])
            else:
                print("Allocating room for:", std["name"])

                allocated_room = None

                # male = Boys hostel rooms starting with B
                # female = Girls hostel rooms starting with G
                for room in rooms:
                    if std["gender"].upper() == "M" and room.startswith("B"):
                        if rooms[room] == "free":
                            allocated_room = room
                            break
                    if std["gender"].upper() == "F" and room.startswith("G"):
                        if rooms[room] == "free":
                            allocated_room = room
                            break

                if allocated_room is None:
                    print("No rooms available for this gender.")
                else:
                    rooms[allocated_room] = "allocated"
                    allocated[roll_num] = allocated_room
                    print("Room allocated:", allocated_room)

    # 3. Reports
    elif choice == "3":
        print("---- ROOM STATUS ----")

        print("All Rooms:")
        for room in rooms:
            print(room, ":", rooms[room])

        print("Allocated Students:")
        for roll in allocated:
            print("Roll:", roll_num, "Room:", allocated[roll_num])

    # 4. Exit
    elif choice == "4":
        print("Exiting system. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
