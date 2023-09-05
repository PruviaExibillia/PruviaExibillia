# Luke Clutts
# This program uses a class to create a GUI CRUD program that allows the user to interact with a phonebook database.

import tkinter
import tkinter.messagebox
import sqlite3

# CRUD_Phonebook class is used to create a GUI for creating, reading, updating, and deleting, entries in a database.
class CRUD_Phonebook:
    
    #  Define the __init__ method.
    def __init__(self):
        # The none_open is used to check if another window is open before opening another.
        self.none_open = True

        # Create the main window and assign it a title.
        self.main = tkinter.Tk()
        self.main.title('Phonebook Database')
        
        # Call mainFrames to create the frames used in the main window. 
        self.mainFrames()
        
        # Call the createList method to create the options listbox.
        self.createList()

        # Create the quit_button for the main frame.
        self.quit_button = tkinter.Button(self.button_frame,
                                          text='Quit All',
                                          command= self.main.destroy)
        
        # Call the pack_frame method to pack the widgets for the main frame. 
        self.pack_frame()

        # Enter the main loop.
        tkinter.mainloop()

    # The get_selection method reads the users selection from the listbox and calls the appropriate method.
    def get_selection(self, event):
        # If a selection is made.
        if self.list.curselection() != ():
            # If no other window is open, open the corrosponding user selection.
            if self.none_open:
                select = self.list.get(self.list.curselection())

                if select == self.list.get(0):
                    self.create()
                elif select == self.list.get(1):
                    self.read()
                elif select == self.list.get(2):
                        self.update()
                elif select == self.list.get(3):
                    self.delete()
            # Or display an error message.
            else:
                tkinter.messagebox.showinfo('Error', 'Only one window may be open at a time.')
    
    # The create method creates a GUI that the user can use to create an new entry in the database.
    def create(self):
        
        # Set none_open to false.
        self.none_open = False

        # Create the window.
        self.window = tkinter.Toplevel(self.main)
        # Create the frames for the current window.
        self.name_f = tkinter.Frame(self.window)
        self.num_f = tkinter.Frame(self.window)
        self.button_f = tkinter.Frame(self.window)
        
        # Create the label and entry box for the name.
        self.name_l = tkinter.Label(self.name_f,
                                     text="Name:     ")
        self.name_e = tkinter.Entry(self.name_f,
                                    width=15)
        # Create the label and entry box for the number.
        self.num_l = tkinter.Label(self.num_f,
                                     text="Number: ")
        self.num_e = tkinter.Entry(self.num_f,
                                    width=15)
        # Create the button to call the insert_query method.
        self.button = tkinter.Button(self.num_f,
                                       text='Create Entry',
                                       command= self.insert_query)
        # Create the buttons to quit window or quit program.
        self.quit_button = tkinter.Button(self.button_f,
                                            text='Quit',
                                            command= self.close_win)
        self.all_button = tkinter.Button(self.button_f,
                                           text='Quit All',
                                           command= self.main.destroy)
        # Pack the widgets for the frame.
        self.name_l.pack(side='left')
        self.name_e.pack(side='left')
        self.num_l.pack(side='left')
        self.num_e.pack(side='left')
        self.button.pack(side='bottom')
        self.quit_button.pack(side='left')
        self.all_button.pack(side='left')
        # Pack the frames for the window.
        self.name_f.pack(anchor='w')
        self.num_f.pack()
        self.button_f.pack()
    
    # The read method creates a GUI that the user can use to return and display 
    # information from the database.
    def read(self):
        # Set none_open to false.
        self.none_open = False
        # Create the window.
        self.window = tkinter.Toplevel(self.main)
        # Create the frames used in the window.
        self.frame = tkinter.Frame(self.window)
        self.button_f = tkinter.Frame(self.window)

        # Create the label and frame for the name entry.
        self.promt = tkinter.Label(self.frame,
                                     text= 'Name: ')
        self.lookup = tkinter.Entry(self.frame,
                                      width=15)
        # Create the button to call the search_query method.
        self.button = tkinter.Button(self.frame,
                                       text='Search',
                                       command= self.search_query)
        # Create the buttons to quit window or quit program.
        self.quit_button = tkinter.Button(self.button_f,
                                            text='Quit',
                                            command= self.close_win)
        self.all_button = tkinter.Button(self.button_f,
                                           text='Quit All',
                                           command= self.main.destroy)
        
        # Packing for the window frames widgets.
        self.promt.pack(side='left')
        self.lookup.pack(side='left')
        self.button.pack()
        self.quit_button.pack(side='left')
        self.all_button.pack(side='left')
        # Packing for the frames.
        self.frame.pack()
        self.button_f.pack()

    # The update method creates a GUI that the user can use to update an entry in the database.
    def update(self):
        # Set none_open to false.
        self.none_open = False
        # Create the window.
        self.window = tkinter.Toplevel(self.main)
        # Create the frames.
        self.name_f = tkinter.Frame(self.window)
        self.num_f = tkinter.Frame(self.window)
        self.button_f = tkinter.Frame(self.window)

        # Create the label and entry for the name entry.
        self.name_l = tkinter.Label(self.name_f,
                                     text="Name:     ")
        self.name_e = tkinter.Entry(self.name_f,
                                    width=15)
        # Create the label and entry for the number entry.
        self.num_l = tkinter.Label(self.num_f,
                                     text="Number: ")
        self.num_e = tkinter.Entry(self.num_f,
                                    width=15)
        # Create the button to call the update_query.
        self.button = tkinter.Button(self.num_f,
                                       text='Update Entry',
                                       command= self.update_query)
        # Create the buttons to quit window or quit program.
        self.quit_button = tkinter.Button(self.button_f,
                                            text='Quit',
                                            command= self.close_win)
        self.all_button = tkinter.Button(self.button_f,
                                           text='Quit All',
                                           command= self.main.destroy)
        
        # Pack the widgets for the frames.
        self.name_l.pack(side='left')
        self.name_e.pack(side='left')
        self.num_l.pack(side='left')
        self.num_e.pack(side='left')
        self.button.pack(side='bottom')
        self.quit_button.pack(side='left')
        self.all_button.pack(side='left')
        # Pack the frames.
        self.name_f.pack(anchor='w')
        self.num_f.pack()
        self.button_f.pack()

    # The delete method create a GUI the user can use to delete a entry from the database.   
    def delete(self):
        # Set none_open to false.
        self.none_open = False
        # Create the window.
        self.window = tkinter.Toplevel(self.main)
        # Create the frames.
        self.name_f = tkinter.Frame(self.window)
        self.button_f = tkinter.Frame(self.window)
        # Create the label and entry for the name entry.
        self.name_l = tkinter.Label(self.name_f,
                                     text="Name: ")
        self.name_e = tkinter.Entry(self.name_f,
                                    width=15)
        # Create the button to run the delete_query method.
        self.button = tkinter.Button(self.name_f,
                                       text='Delete Entry',
                                       command= self.delete_query)
        # Create the buttons to quit window or quit program.
        self.quit_button = tkinter.Button(self.button_f,
                                            text='Quit',
                                            command= self.close_win)
        self.all_button = tkinter.Button(self.button_f,
                                           text='Quit All',
                                           command= self.main.destroy)
        
        # Pack the widgets.
        self.name_l.pack(side='left')
        self.name_e.pack(side='left')
        self.button.pack(side='bottom')
        self.quit_button.pack(side='left')
        self.all_button.pack(side='left')
        # Pack the frames.
        self.name_f.pack()
        self.button_f.pack()

    # The search_query method querys the database for a user inputted name and display the associated data.
    def search_query(self):
        # Set conn to None
        conn = None
        # Assign the entry from the user to the search variable.
        search = str(self.lookup.get())
        try:
            # Connect to the database and create a cursor 
            conn = sqlite3.connect("phonebook.db")
            cur = conn.cursor()

            # Select all the information about the user inputted name from the database. 
            cur.execute("SELECT * FROM Entries WHERE NAME = ?",(search,))
            # Store the results of the query in the results variable.
            results = cur.fetchone()
            # If results is not nothing create a message box to display the information about the quered entry.
            if results != None:
                tkinter.messagebox.showinfo('Results', f'ID: {results[0]}\nName: {results[1]}\nPhone Number: {results[2]}')
                # Clear the entry box.
                self.lookup.delete(0, 'end')
            # Otherwise display and error messagebox.
            else:
                tkinter.messagebox.showinfo('Error ', 'Name: ' + search + ' not found in database.')
        # If an error is raised by the database display it.
        except sqlite3.Error as err:
            tkinter.messagebox.showinfo('Database Error', err)

        # Close the connection to the database   
        finally:
            if conn != None:
                conn.close()

    # The insert_query method creates a new entry into the database using user inputted information.
    def insert_query(self):
        # Set conn to None.
        conn = None
        # Get the name and number from the user inputted entries.
        name = str(self.name_e.get())
        number = str(self.num_e.get())
        try:
            # Connect to the database and create a cursor
            conn = sqlite3.connect("phonebook.db")
            cur = conn.cursor()
            # Insert the information into the table.
            cur.execute('''INSERT INTO Entries (Name, Phone)
                           VALUES(?,?)''',(name, number,))
            # Apply the changes.
            conn.commit()

            # Inform the user the operation was succseful
            tkinter.messagebox.showinfo('Update', 'Entry created for ' + name + ' with number ' + number +'.')
            self.name_e.delete(0, 'end')
            self.num_e.delete(0, 'end')

        # If an error is raised by the database display it.
        except sqlite3.Error as err:
            tkinter.messagebox.showinfo('Database Error', err)
        
        # Close the connection to the database.
        finally:
            if conn != None:
                conn.close()
        
    # The update_query creates a GUI the user can use to update the number of an entry in the database.
    def update_query(self):
        # Set conn to None.
        conn = None
        # Get the name and number from the user inputted entries.
        name = str(self.name_e.get())
        number = str(self.num_e.get())
        try:
            # Connect to the database and create a cursor.
            conn = sqlite3.connect("phonebook.db")
            cur = conn.cursor()
            # Update the entry witht he new number from the inputted from the user.
            cur.execute('''UPDATE Entries SET Phone = ? WHERE Name = ?''',(number, name,))
            # Apply the changes.
            conn.commit()

            # If the number of changes to the datbase is more than zero inform the user the entry was updated successfully.
            if conn.total_changes > 0:
                tkinter.messagebox.showinfo('Update', name + ' number was successfully updated')
                self.name_e.delete(0, 'end')
                self.num_e.delete(0, 'end')
            # Otherwise inform the user that the name could not be found in the database
            else:
                tkinter.messagebox.showinfo('Error', name + " was not found in the database")

        # If an error is raised by the database display it.
        except sqlite3.Error as err:
            tkinter.messagebox.showinfo('Database Error', err)

        # Close the connection to the database.
        finally:
            if conn != None:
                conn.close()

    # The delete_query creates a GUI that the user can use to delete an entry from the database.
    def delete_query(self):
        # Set conn to None.
        conn = None
        # Get the name from the user entry box.
        name = str(self.name_e.get())
        
        try:
            # Connect to the database and create a cursor.
            conn = sqlite3.connect("phonebook.db")
            cur = conn.cursor()

            # Delete the entry from the database using the name entered by the user.
            cur.execute('''DELETE FROM Entries WHERE Name = ?''',
                        (name,))
            # Apply the changes
            conn.commit()

            # Get the number of rows deleted from the database.
            num_delete = cur.rowcount
            
            # If the number of rows deleted is larger than 0 inform the user how many entries were deleted.
            if num_delete > 0:
                tkinter.messagebox.showinfo('Update', 'Successfully deleted '+ str(num_delete) + ' row(s)')
                self.name_e.delete(0, 'end')
            # Otherwise inform the user no entrys were found with inputted name.
            else:
                tkinter.messagebox.showinfo('Error', 'No Entries found with name ' + name + '.')

        # If the database raises an error display it.
        except sqlite3.Error as err:
            tkinter.messagebox.showinfo('Database Error', err)
        
        # Close the connection to the database.
        finally:
            if conn != None:
                conn.close()
    
    # The close_win function close the currently opened window and allow the opening of other windows.
    def close_win(self):
        # Set none_open to true.
        self.none_open = True
        # Destroy the window.
        self.window.destroy()

    # mainFrames creates the frames for the main window.
    def mainFrames(self):
        self.title_frame = tkinter.Frame(self.main)
        self.list_frame = tkinter.Frame(self.main)
        self.button_frame = tkinter.Frame(self.main)

    # createList creates the list box and populates it.
    def createList(self):
        # Create a title for the list box.
        self.title_label = tkinter.Label(self.title_frame,
                                         text='Select an option:')
        # Create the listbox.
        self.list = tkinter.Listbox(self.list_frame,
                                    selectmode= tkinter.SINGLE,
                                    height=6,
                                    width=30)
        
        # Populate the listbox.
        self.list.insert(1,"Create new Entries")
        self.list.insert(2,"Look up Phone Numbers")
        self.list.insert(3,"Update Phone Numbers")
        self.list.insert(4,"Delete Entries")

        # Assign the get_selection function to the action of the user selecting a choice.
        self.list.bind('<<ListboxSelect>>', self.get_selection)

    # pack_frame packs all the widgets and frames for the main window.
    def pack_frame(self):
        self.title_label.pack()
        self.list.pack()
        self.quit_button.pack()
        self.title_frame.pack()
        self.list_frame.pack()
        self.button_frame.pack()

# Create an instance of StateInfoGUI.
if __name__ == "__main__":
    test = CRUD_Phonebook()
