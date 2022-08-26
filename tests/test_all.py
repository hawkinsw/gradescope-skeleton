from gradescope_utils.autograder_utils.decorators import weight, tags, visibility
from gradesucope.gradesucope import FileExistsTestCase, FileContentsMatchTestCase

class DocumentsTestCase(FileExistsTestCase):
    @weight(1)
    # A mandatory tag means that if the student does not get any points for
    # this test, then they cannot get any points for anything. The other
    # tests will be scored, but their total score will ultimately be 0. I
    # have found that marking checks for whether they have submitted all
    # the required files as mandatory makes it blaringly obvious to the
    # student that they are missing something and makes it harder for
    # them to accidentally forget submitting a file that is otherwise
    # not tested in later checks.
    @tags("mandatory")
    def test_design_pdf(self):
        """This text will be displayed to the student next to their score on this metric."""
        # Check to see whether their submission contains the file given
        # as a parameter. Not that the file must have been transferred
        # to the /autograder/source directory by run_autograder. Otherwise,
        # use the path named parameter in order to customize where
        # the function should search for it on the filesystem.
        self.file_exists("afile.ext")

class NamePromptTestCase(FileContentsMatchTestCase):
    @weight(39)
    @tags("mandatory")
    def test_name_prompt(self):
      """This text will be displayed to the student next to their score on this metric."""
      # Make it so that only the text given as the msg parameter to 
      # assertXXX functions are displayed when the assertion fails. Not
      # setting this member will cause output to be given before the
      # custom message that (I've found) confuses students.
      self.longMessage = False

      # Run some test to check whether their assignment submission is
      # correct.
      count = self.count_file_matches("pseudocode.txt", "^Name: ")

      # Check whether their assignment is correct and output a message
      # (that the student will see on the screen) if their submission is
      # wrong.
      self.assertGreater(count, 0, msg="I expected at least one line that started with 'Name: ', but you gave me " + str(count) + " such lines.")
