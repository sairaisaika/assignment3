"# assignment3  
Assignment 03 – Proof of Concept Delivery – See Brightspace for due dates  
Refer to the Course Section Information (CSI) document posted in Brightspace under Course  
Information for additional requirements common to all assignments.  
Tasks  
 See the Course Section Information document for details on the required use of the data set.  
 You may use your Exercise 3 code as a reference / starting-point but I expect modifications, i.e.  
   passing in exercise 3 a second time with very small changes will not earn marks.  
 Write a simple program, in your language of study that completes the following tasks:  
    o Uses File-IO on startup to open the dataset, read in up to the first 200 records of data (if there  
      are more than that), and store each one in a Record Object which collectively in turn are stored  
      into a simple data structure (array or a list), use exception handling in case the file is missing  
      or not available.  
    o The first one or two records may have column names, these can be shown on screen but  
      should not be placed into the simple data structure. Note: Column names may be provided in  
      French as well as English, use only the English names in your program.  
    o See the documents included in the dataset area in Brightspace for the list of columns to  
      use, note that all listed columns need to be used, and need to be present within your  
      source code to verify you are using the dataset provided.  
    o Displays your full name on screen so it remains visible at all times, or after each user  
      interaction.  
    o Is architected in layers e.g. Presentation, Business, Persistence with record-objects (also  
      known as Model or Entity objects)  
    o Provide the user the options and functionality to:  
         Reload the data from the dataset, replacing the in-memory data  
         Persist the data from memory, with any changes, to the disk as a comma separated file,  
          writing to a new file.  
         Display all the records held in the simple data structure (keep it to 200 for testing), but  
          endeavor to load all records from the file. (You will need to load all records in later  
          work).  
         Create a new record and store it in the simple data structure  
         Select, display and edit a record held in the simple data structure  
         Delete a record from the simple data structure  
    o Take a screen shot of your program performing each task above, ensuring your full name is  
      within each screen shot.  
    o Comment your source code file using documentation comments (docstrings in Python, XMLdocument  
       in C# or VB.Net etc.)  
 Write a single unit-test using a testing framework to test one part of your program.  
    o Assignment 3 Unit-Test Examples (you would only do one, or a similar test):  
         Is the first record, with data values, read from the dataset what we expect?  
         Is a new record added to the end of the array or list within the Business layer?  
         When a record is edited are the changes to the record within the array or list correct?  
         When a record is deleted from the array or list was it actually removed?  
         If the file cannot be located is an exception raised / caught / handled?  
         Etc.  
    o Comment your unit-test source code using documentation comments (docstrings in Python,  
      XML-document in C# or VB.Net etc.)  
 Your program should use the following programming concepts: variable, a loop structure, a decision  
   structure, File-IO reading from the dataset, File-IO writing a csv file, exception handling, use of an API  
   library, an array (or similar data structure), and unit testing  
 Document your learning, demonstrate that your program runs and is unit tested with screen shots,  
   and include the source code with your programmer comments within a single MS Word document.  
   Also include the original source code files as part of your submission. See the expected format,  
   submission requirements, and grading guide below.  
 Video Game Software projects are not acceptable in this course.  
   Your single MS Word document should have this general format  
 Cover page with your full name within it.  
 Heading with name “1 Evidence of Learning”  
    o Code figures to demonstrate use of variables, a loop structure, a decision structure, File-IO  
      against the dataset, exception handling, use of an API library, an array (or similar data  
      structure) and unit testing.  
    o Either:
         Use small code examples for each topic, or
         Indicate what line numbers in a larger code sample illustrate each concept.
         You must indicate clearly to your professor that you can identify what parts of
          your code illustrate and match to each programming concept.
 Heading with name “2 Program Architecture”
    o Briefly outline how your modules / classes / code files are organized into layers or similar
      architectural design. UML Diagrams are needed as part of your write up. See this website as a
      quick example / review as well as see notes inside the rubric as well.
      https://www.uml-diagrams.org/multi-layered-application-uml-model-diagram-example.html
      Note that a single source code file, with methods, is not layered. It needs to be broken out into
      separate files / classes / modules. See the example provided on Brightspace.
 Heading with name “3 Program Demonstration via Screen Shots”
    o Include screen shots of your running program, I should see records from the data set
      displayed, as well as creating, updating, deleting records and re-loading and saving records.
      Your full name must appear within the screen shots.
 Heading with name “4 Unit Testing Demonstration via Screen Shots”
    o Include screen shot(s) of your running unit test(s), this may be either within an IDE or run
      from a console. Your full name must appear within the screen shot(s).
 Heading with name “5 Source Code Commenting Example”
    o Copy and paste one source code file from your project to demonstrate you can write
      programming comments using documentation-comments. Use a font size of 10 point, with a
      monospaced font of your choosing.
    o Also copy and paste your unit test source code file, including programmer comments into this
      section. Use a font size of 10 point, with a monospaced font of your choosing.
    o Note: Some frameworks generate many code files, many of them will never be edited by you.
      Only include a source code file you created or edited yourself as well as a unit test code file you
      created or edited within the MS Word document.
 Do not copy and paste code from the web into your demonstration program, it must be your own
   work." 