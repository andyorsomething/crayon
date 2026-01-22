import colorama
from colorama import Fore, Style
colorama.init()
import os
import tkinter as tk
from tkinter import filedialog

####### DEFAULT VALUE SECTION #######

ColorHexInputString = Style.DIM + "(Leave field empty to return to main menu)" + Style.RESET_ALL + "\nEnter the color hex: "
EditingHighHPString = "\nEditing High Health Survivor Glow Color\n"
EditingMediumHPString = "\nEditing Medium Health Survivor Glow Color\n"
EditingLowHPString = "\nEditing Low Health Survivor Glow Color\n"
EditingCriticalHPString = "\nEditing Critical Health Survivor Glow Color\n"
EditingNormalString = "\nEditing Normal Survivor Glow Color\n"
EditingVomitString = "\nEditing Survivor Covered in Vomit Glow Color\n"
EditingHurtString = "\nEditing Injured Survivor Glow Color\n"
EditingItemString = "\nEditing Item Glow Color\n"
EditingFarItemString = "\nEditing Far Item Glow Color\n"
EditingThirdStrikeItemString = "\nEditing Third Strike Item Glow Color\n"
EditingInfectedString = "\nEditing Infected Glow Color\n"
EditingGhostInfectedString = "\nEditing Special Infected Ghost Glow Color\n"
EditingSurvivorVomitString = "\nEditing Survivor Covered in Vomit Glow Color\n"
ReturnToMainMenuString = Style.DIM + "Press Enter to return to the main menu..." + Style.RESET_ALL
OptionInputString = "Please enter an option: "

CONFIG_VALIDATION_KEY = "// L4D2_GLOW_COLORCHANGER_VALID_CONFIG"

variables = {
    "cl_glow_survivor_r": 0.3, ##### SURVIVOR POV GLOWS #####
    "cl_glow_survivor_g": 0.4,
    "cl_glow_survivor_b": 1.0,
    "cl_glow_survivor_vomit_r": 1.0,
    "cl_glow_survivor_vomit_g": 0.4,
    "cl_glow_survivor_vomit_b": 0.0,
    "cl_glow_survivor_hurt_r": 1.0,
    "cl_glow_survivor_hurt_g": 0.4,
    "cl_glow_survivor_hurt_b": 0.0,
    "cl_glow_ability_r": 1.0,
    "cl_glow_ability_g": 0.0,
    "cl_glow_ability_b": 0.0,
    "cl_glow_item_r": 1.0, ##### ITEM GLOWS #####
    "cl_glow_item_g": 1.0,
    "cl_glow_item_b": 1.0,
    "cl_glow_item_far_r": 0.3,
    "cl_glow_item_far_g": 0.4,
    "cl_glow_item_far_b": 1.0,
    "cl_glow_thirdstrike_item_r": 1.0,
    "cl_glow_thirdstrike_item_g": 0.0,
    "cl_glow_thirdstrike_item_b": 0.0,

    "cl_glow_infected_vomit_r": 0.79, ##### INFECTED POV GLOWS #####
    "cl_glow_infected_vomit_g": 0.07, # Survivors covered in vomit from SI POV
    "cl_glow_infected_vomit_b": 0.72,
    "cl_glow_ghost_infected_r": 0.3, # Outline of SI before they've spawned
    "cl_glow_ghost_infected_g": 0.4,
    "cl_glow_ghost_infected_b": 1.0,
    "cl_glow_survivor_health_high_r": 0.039,
    "cl_glow_survivor_health_high_g": 0.0,
    "cl_glow_survivor_health_high_b": 0.0,
    "cl_glow_survivor_health_med_r": 0.59,
    "cl_glow_survivor_health_med_g": 0.45,
    "cl_glow_survivor_health_med_b": 0.032,
    "cl_glow_survivor_health_low_r": 0.70,
    "cl_glow_survivor_health_low_g": 0.25,
    "cl_glow_survivor_health_low_b": 0.0,
    "cl_glow_survivor_health_crit_r": 0.63,
    "cl_glow_survivor_health_crit_g": 0.098,
    "cl_glow_survivor_health_crit_b": 0.098,
}

####### FUNCTION SECTION #######

def get_valid_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            return 0

# First, let's welcome and ask the user what they want to do
def OpeningPrompt():
    ClearScreen()
    print("Welcome to " + Fore.LIGHTYELLOW_EX + "Crayon" + Fore.RESET + ", an automated outline color changer for Left 4 Dead 2!")
    print("Make sure you have your desired color codes ready!\n")
    print("1. Survivor POV Outlines - " + Style.DIM + "Change the colors of survivor outlines you see while playing as a survivor.\n" + Style.RESET_ALL)
    print("2. Infected POV Outlines - " + Style.DIM + "Change the colors of survivor outlines you see while playing as an infected.\n" + Style.RESET_ALL)
    print("3. Item Outlines - " + Style.DIM + "Change the outline colors of interactable items.\n" + Style.RESET_ALL)
    print("4. Import Config - " + Style.DIM + "Import a config file. This will override your current settings.\n" + Style.RESET_ALL)
    print("5. Export Config - " + Style.DIM + "Saves your custom colors to a config file.\n" + Style.RESET_ALL)
    print("6. About - " + Style.DIM + "View information about this program.\n" + Style.RESET_ALL)
    print("7. Exit - " + Style.DIM + "Closes the program.\n" + Style.RESET_ALL)
    option = get_valid_integer_input(OptionInputString)
    # We check what the user's option is and call the appropriate function
    if option == 7:
        ClearScreen()
        exit()
    ClearScreen()
    if option < 8 and option > 0 :
        GlowColorChanger(option)
    else:
        ClearScreen()
        OpeningPrompt()


# Second, let's show the options for survivor glows
def GlowColorChanger(inputOption):
    subOption = 0
    ColorHex = ""
    WantsToExit = False
    while WantsToExit == False:
        if inputOption == 1:
            print("Survivor POV Outline Colors\n\n")
            print("1. Edit Normal Survivor Outline Color - " + Style.DIM + "The outline that appears around a survivor that is distant or behind a wall.\n" + Style.RESET_ALL)
            print("2. Edit Survivor Covered in Vomit Outline Color - " + Style.DIM + "The outline that appears around a survivor covered in vomit.\n" + Style.RESET_ALL)
            print("3. Edit Downed Survivor Outline Color - " + Style.DIM + "The outline that appears around a downed survivor.\n" + Style.RESET_ALL)
            print("4. Edit Special Infected Outline Color - " + Style.DIM + "The outline that appears around a special infected attacking a survivor.\n" + Style.RESET_ALL)
            print("5. Return to Main Menu\n")
            subOption = get_valid_integer_input(OptionInputString)
            # We check what the user's sub-option is and call the appropriate function
            if subOption == 1:
                print(EditingNormalString)
                while len(ColorHex) < 6:
                    ColorHex = input(ColorHexInputString)
                    if ColorHex == "":
                        OpeningPrompt()
                    elif len(ColorHex) < 6:
                        print("Invalid color hex\n")
                        continue    
                    else:
                        variables["cl_glow_survivor_r"] = ColorParser(ColorHex)[0]
                        variables["cl_glow_survivor_g"] = ColorParser(ColorHex)[1]
                        variables["cl_glow_survivor_b"] = ColorParser(ColorHex)[2]
                        print(f"\nNormal Survivor Outline Color set to {ColorHex}")
                        input(ReturnToMainMenuString)
                        OpeningPrompt()
            elif subOption == 2:
                print(EditingVomitString)
                while len(ColorHex) < 6:
                    ColorHex = input(ColorHexInputString)
                    if ColorHex == "":
                        OpeningPrompt()
                    elif len(ColorHex) < 6:
                        print("Invalid color hex\n")
                        continue
                    else:
                        variables["cl_glow_survivor_vomit_r"] = ColorParser(ColorHex)[0]
                        variables["cl_glow_survivor_vomit_g"] = ColorParser(ColorHex)[1]
                        variables["cl_glow_survivor_vomit_b"] = ColorParser(ColorHex)[2]
                        print(f"\nSurvivor Covered in Vomit Outline Color set to {ColorHex}")
                        input(ReturnToMainMenuString)
                        OpeningPrompt()
            elif subOption == 3:
                print(EditingHurtString)
                while len(ColorHex) < 6:
                    ColorHex = input(ColorHexInputString)
                    if ColorHex == "":
                        OpeningPrompt()
                    elif len(ColorHex) < 6:
                        print("Invalid color hex\n")
                        continue
                    else:
                        variables["cl_glow_survivor_hurt_r"] = ColorParser(ColorHex)[0]
                        variables["cl_glow_survivor_hurt_g"] = ColorParser(ColorHex)[1]
                        variables["cl_glow_survivor_hurt_b"] = ColorParser(ColorHex)[2]
                        print(f"\nDowned Survivor Outline Color set to {ColorHex}")
                        input(ReturnToMainMenuString)
                        OpeningPrompt()
            elif subOption == 4:
                print(EditingInfectedString)
                while len(ColorHex) < 6:
                    ColorHex = input(ColorHexInputString)
                    if ColorHex == "":
                        OpeningPrompt()
                    elif len(ColorHex) < 6:
                        print("Invalid color hex\n")
                        continue
                    else:
                        variables["cl_glow_ability_r"] = ColorParser(ColorHex)[0]
                        variables["cl_glow_ability_g"] = ColorParser(ColorHex)[1]
                        variables["cl_glow_ability_b"] = ColorParser(ColorHex)[2]
                        print(f"\nSpecial Infected Attacking Survivor Outline Color set to {ColorHex}")
                        input(ReturnToMainMenuString)
                        OpeningPrompt()
            elif subOption == 5:
                OpeningPrompt()
            else:
                ClearScreen()
                continue

        elif inputOption == 2:
            print("Infected POV Outline Colors\n\n")
            print("1. Edit Survivor Covered in Vomit Outline Color - " + Style.DIM + "The outline that appears around a survivor covered in vomit.\n" + Style.RESET_ALL)
            print("2. Edit Special Infected Ghost Outline Color - " + Style.DIM + "The outline that appears around an unspawned special infected teammate.\n" + Style.RESET_ALL)
            print("3. Edit Survivor High Health Outline Color - " + Style.DIM + "The outline that appears around a survivor with 40+ HP.\n" + Style.RESET_ALL)
            print("4. Edit Survivor Medium Health Outline Color - " + Style.DIM + "The outline that appears around a survivor with 25-40 HP.\n" + Style.RESET_ALL)
            print("5. Edit Survivor Low Health Outline Color - " + Style.DIM + "The outline that appears around a survivor with less than 25 HP.\n" + Style.RESET_ALL)
            print("6. Edit Survivor Critical Health Outline Color - " + Style.DIM + "The outline that appears around an incapacitated survivor.\n" + Style.RESET_ALL)
            print("7. Return to Main Menu\n")
            subOption = get_valid_integer_input(OptionInputString)
            if subOption == 1:
                print(EditingSurvivorVomitString)
                while len(ColorHex) < 6:
                    ColorHex = input(ColorHexInputString)
                    if ColorHex == "":
                        OpeningPrompt()
                    elif len(ColorHex) < 6:
                        print("Invalid color hex\n")
                        continue    
                    else:
                        variables["cl_glow_infected_vomit_r"] = ColorParser(ColorHex)[0]
                        variables["cl_glow_infected_vomit_g"] = ColorParser(ColorHex)[1]
                        variables["cl_glow_infected_vomit_b"] = ColorParser(ColorHex)[2]
                        print(f"\nSurvivor Covered in Vomit Outline Color set to {ColorHex}")
                        input(ReturnToMainMenuString)
                        OpeningPrompt()
            elif subOption == 2:
                print(EditingGhostInfectedString)
                while len(ColorHex) < 6:
                    ColorHex = input(ColorHexInputString)
                    if ColorHex == "":
                        OpeningPrompt()
                    elif len(ColorHex) < 6:
                        print("Invalid color hex\n")
                        continue
                    else:
                        variables["cl_glow_ghost_infected_r"] = ColorParser(ColorHex)[0]
                        variables["cl_glow_ghost_infected_g"] = ColorParser(ColorHex)[1]
                        variables["cl_glow_ghost_infected_b"] = ColorParser(ColorHex)[2]
                        print(f"\nGhost Infected Outline Color set to {ColorHex}")
                        input(ReturnToMainMenuString)
                        OpeningPrompt()
            elif subOption == 3:
                print(EditingHighHPString)
                while len(ColorHex) < 6:
                    ColorHex = input(ColorHexInputString)
                    if ColorHex == "":
                        OpeningPrompt()
                    elif len(ColorHex) < 6:
                        print("Invalid color hex\n")
                        continue    
                    else:
                        variables["cl_glow_survivor_health_high_r"] = ColorParser(ColorHex)[0]
                        variables["cl_glow_survivor_health_high_g"] = ColorParser(ColorHex)[1]
                        variables["cl_glow_survivor_health_high_b"] = ColorParser(ColorHex)[2]
                        print(f"\nHigh Health Outline Color set to {ColorHex}")
                        input(ReturnToMainMenuString)
                        OpeningPrompt()
            elif subOption == 4:
                print(EditingMediumHPString)
                while len(ColorHex) < 6:
                    ColorHex = input(ColorHexInputString)
                    if ColorHex == "":
                        OpeningPrompt()
                    elif len(ColorHex) < 6:
                        print("Invalid color hex\n")
                        continue    
                    else:
                        variables["cl_glow_survivor_health_medium_r"] = ColorParser(ColorHex)[0]
                        variables["cl_glow_survivor_health_medium_g"] = ColorParser(ColorHex)[1]
                        variables["cl_glow_survivor_health_medium_b"] = ColorParser(ColorHex)[2]
                        print(f"\nMedium Health Outline Color set to {ColorHex}")
                        input(ReturnToMainMenuString)
                        OpeningPrompt()
            elif subOption == 5:
                print(EditingLowHPString)
                while len(ColorHex) < 6:
                    ColorHex = input(ColorHexInputString)
                    if ColorHex == "":
                        OpeningPrompt()
                    elif len(ColorHex) < 6:
                        print("Invalid color hex\n")
                        continue    
                    else:
                        variables["cl_glow_survivor_health_low_r"] = ColorParser(ColorHex)[0]
                        variables["cl_glow_survivor_health_low_g"] = ColorParser(ColorHex)[1]
                        variables["cl_glow_survivor_health_low_b"] = ColorParser(ColorHex)[2]
                        print(f"\nLow Health Outline Color set to {ColorHex}")
                        input(ReturnToMainMenuString)
                        OpeningPrompt()
            elif subOption == 6:
                print(EditingCriticalHPString)
                while len(ColorHex) < 6:
                    ColorHex = input(ColorHexInputString)
                    if ColorHex == "":
                        OpeningPrompt()
                    elif len(ColorHex) < 6:
                        print("Invalid color hex\n")
                        continue    
                    else:
                        variables["cl_glow_survivor_health_crit_r"] = ColorParser(ColorHex)[0]
                        variables["cl_glow_survivor_health_crit_g"] = ColorParser(ColorHex)[1]
                        variables["cl_glow_survivor_health_crit_b"] = ColorParser(ColorHex)[2]
                        print(f"\nDowned/Critical Health Outline Color set to {ColorHex}")
                        input(ReturnToMainMenuString)
                        OpeningPrompt()
            elif subOption == 7:
                OpeningPrompt()
            else:
                ClearScreen()
                continue
        elif inputOption == 3:
            print("Item Glow Colors\n\n")
            print("1. Edit Regular Item Outline - " + Style.DIM + "The outline that appears around an item that is within reach.\n" + Style.RESET_ALL)
            print("2. Edit Far Item Outline - " + Style.DIM + "The outline that appears around an item that is nearby.\n" + Style.RESET_ALL)
            print("3. Edit Black and White Item Outline - " + Style.DIM + "The outline that appears around an item while you're near death.\n" + Style.RESET_ALL)
            print("4. Return to Main Menu\n")
            subOption = get_valid_integer_input(OptionInputString)
            if subOption == 1:
                print(EditingItemString)
                while len(ColorHex) < 6:
                    ColorHex = input(ColorHexInputString)
                    if ColorHex == "":
                        OpeningPrompt()
                    elif len(ColorHex) < 6:
                        print("Invalid color hex\n")
                        continue
                    else:
                        variables["cl_glow_item_r"] = ColorParser(ColorHex)[0]
                        variables["cl_glow_item_g"] = ColorParser(ColorHex)[1]
                        variables["cl_glow_item_b"] = ColorParser(ColorHex)[2]
                        print(f"\nRegular Item Outline Color set to {ColorHex}")
                        input(ReturnToMainMenuString)
                        OpeningPrompt()
            elif subOption == 2:
                print(EditingFarItemString)
                while len(ColorHex) < 6:
                    ColorHex = input(ColorHexInputString)
                    if ColorHex == "":
                        OpeningPrompt()
                    elif len(ColorHex) < 6:
                        print("Invalid color hex\n")
                        continue
                    else:
                        variables["cl_glow_item_far_r"] = ColorParser(ColorHex)[0]
                        variables["cl_glow_item_far_g"] = ColorParser(ColorHex)[1]
                        variables["cl_glow_item_far_b"] = ColorParser(ColorHex)[2]
                        print(f"\nFar Item Outline Color set to {ColorHex}")
                        input(ReturnToMainMenuString)
                        OpeningPrompt()
            elif subOption == 3:
                print(EditingThirdStrikeItemString)
                while len(ColorHex) < 6:
                    ColorHex = input(ColorHexInputString)
                    if ColorHex == "":
                        OpeningPrompt()
                    elif len(ColorHex) < 6:
                        print("Invalid color hex\n")
                        continue
                    else:
                        variables["cl_glow_thirdstrike_item_r"] = ColorParser(ColorHex)[0]
                        variables["cl_glow_thirdstrike_item_g"] = ColorParser(ColorHex)[1]
                        variables["cl_glow_thirdstrike_item_b"] = ColorParser(ColorHex)[2]
                        print(f"\nBlack and White Item Outline Color set to {ColorHex}")
                        input(ReturnToMainMenuString)
                        OpeningPrompt()
            elif subOption == 4:
                OpeningPrompt()
            else:
                ClearScreen()
                continue
        elif inputOption == 4:
            ImportConfig()
        elif inputOption == 5:
            WriteToConfig()
        elif inputOption == 6:
            Help() # help section
        else:
            ClearScreen()
            continue

def ColorParser(ColorCodeinHex):
    # Convert hex to rgb
    if ColorCodeinHex.startswith("#"):
        ColorCodeinHex = ColorCodeinHex[1:]
    red = int(ColorCodeinHex[0:2], 16) / 255
    green = int(ColorCodeinHex[2:4], 16) / 255
    blue = int(ColorCodeinHex[4:6], 16) / 255

    return red,green,blue

def CreateAutoexec(created_file_path):
    # 1. Get the directory and filename
    directory = os.path.dirname(created_file_path)
    filename = os.path.basename(created_file_path)

    # 2. Check if autoexec.cfg already exists
    autoexec_path = os.path.join(directory, "autoexec.cfg")
    
    if os.path.exists(autoexec_path):
        print(f"\n{Fore.YELLOW}WARNING: An 'autoexec.cfg' file already exists at:\n{autoexec_path}{Fore.RESET}\n")
        print("Do you want to overwrite it? (Y/N)")
        print(f"{Style.DIM}(Selecting 'N' will append the exec command to the existing file instead){Style.RESET_ALL}")
        
        while True:
            choice = input(OptionInputString).strip().upper()
            if choice == 'Y':
                # Overwrite
                with open(autoexec_path, "w") as f:
                    f.write(f'exec "{filename}"')
                print(f"\n{Fore.CYAN}'autoexec.cfg' has been overwritten.{Fore.RESET}\n")
                break
            elif choice == 'N':
                # Append
                with open(autoexec_path, "a") as f:
                    f.write(f'\nexec "{filename}"')
                print(f"\n{Fore.CYAN}Added exec command to existing 'autoexec.cfg'.{Fore.RESET}\n")
                break
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")
    else:
        # Create new
        with open(autoexec_path, "w") as f:
            f.write(f'exec "{filename}"')
        print(f"\n{Fore.CYAN}Companion 'autoexec.cfg' created at:\n{autoexec_path}{Fore.RESET}\n")

def WriteToConfig():
    # Hide the main tkinter window that pops up by default
    root = tk.Tk()
    root.withdraw()

    # Open the "Save As" dialog
    file_path = filedialog.asksaveasfilename(
        defaultextension=".cfg",
        filetypes=[("Config files", "*.cfg")],
        initialfile="custom_outline_colors.cfg", # Suggested name
        title="Choose where to save your variables"
    )

    # Check if the user didn't just hit "Cancel"
    if file_path:
        with open(file_path, "w") as f:
            f.write(f"{CONFIG_VALIDATION_KEY}\n")
            for key, value in variables.items():
                f.write(f"{key} {value}\n")
        print(f"{Fore.GREEN}File saved successfully!{Fore.RESET}\nIt can be found at:\n{file_path}")
        CreateAutoexec(file_path)
        input(ReturnToMainMenuString)
    else:
        pass
    OpeningPrompt()

def ImportConfig():
    # Hide the main tkinter window that pops up by default
    root = tk.Tk()
    root.withdraw()

    # Open the "Open" dialog
    file_path = filedialog.askopenfilename(
        defaultextension=".cfg",
        filetypes=[("Config files", "*.cfg")],
        initialfile="custom_outline_colors.cfg", # Suggested name
        title="Select an existing config file"
    )

    # Check if the user didn't just hit "Cancel"
    if file_path:
        with open(file_path, "r") as f:
            lines = f.readlines()
            if not lines or lines[0].strip() != CONFIG_VALIDATION_KEY:
                print(f"{Fore.RED}This config file is not compatible with this program.{Fore.RESET}\n")
                input(ReturnToMainMenuString)
                OpeningPrompt()
                return

            for line in lines[1:]: # Skip the first line (key)
                if not line.strip(): continue
                try:
                    key, value = line.strip().split(" ")
                    if key in variables:
                        variables[key] = value
                except ValueError:
                    continue # Skip malformed lines

        print(f"{Fore.GREEN}File imported successfully!{Fore.RESET}\n")
        input(ReturnToMainMenuString)
    else:
        pass
    OpeningPrompt()

def Help():
    ClearScreen()
    # introduction
    print("This program allows you to change the outline colors of select entities in Left 4 Dead 2,\nletting you export a config file to a location of your choice.\n")
    # features
    print(Fore.LIGHTYELLOW_EX + "When changing any outline color, be sure to use a color in the hex format.\nYou can use an online color picker (like coolors.co) to easily retrieve any color's hex value.\n")
    print("NOTE: While colors with a lower value/brightness may work,\nit's recommended to use colors with a higher value for better visibility.\n" + Fore.RESET)
    # import and export
    print("If you've previously used this program to create a config, you can import it back into the program to edit your colors.\n")
    print(Fore.LIGHTRED_EX + "It should be noted that importing a config file requires the file to have\nthe same formatting as any config file exported by this program,\notherwise it will not import properly.\n" + Fore.RESET)
    print("Exporting a config without any edits will create a config file with all the default values.\nThis is useful for creating a config that resets your colors.\n")
    input(ReturnToMainMenuString)
    OpeningPrompt()

def ClearScreen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux (os.name is 'posix')
    else:
        os.system('clear')


if __name__ == "__main__":
    OpeningPrompt()

