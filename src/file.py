import os

class FileHandler:
    """ A class to handle the opening/closing and reading/writing of a file.

    Attributes
    ----------
    None

    Methods
    -------
    read():
        Returns the contents of the file.

    write(text):
        Writes the provided text to the file.

    append(text):
        Appends the provided text to the file.

    read_lines():
        Returns the lines of the file.

    write_lines(lines):
        Writes the provided lines to the file.
    """
    def __init__(self):
        self._path = ''

    # GETTERS/SETTERS
    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        if isinstance(value, str) and os.path.splitext(value)[1]:
            self._path = value
        else:
            raise ValueError('Invalid file path attribute specified')

    # HELPER METHODS
    def _file_handler(self, method='read', param=None):
        """ Handles the opening/closing and reading/writing of the file.

        Parameters
        ----------
            method: str
                The file method to perform (default is ``'read'``).

            param: varies
                Optional parameter, provides the necessary parameters to perform the file method.

        Returns
        -------
        ``None`` or the file data.
        """
        try:
            mode = method[0]
            with open(self._path, mode) as f:
                if method == 'read':
                    return f.read()
                elif method in ('write', 'append'):
                    f.write(param)
                elif method == 'read_lines':
                    return f.readlines()
                elif method == 'write_lines':
                    for line in param:
                        f.write(line)
        except FileNotFoundError:
            raise AttributeError('File does not exist')

    # USER METHODS
    def read(self):
        """ Reads the contents of the file.

        Returns
        -------
        str
            The file content.
        """
        return self._file_handler()

    def write(self, text):
        """ Writes the provided text to the file.

        Parameters
        ----------
        text: str
            The text to write.

        Returns
        -------
        None
        """
        self._file_handler('write', text)

    def append(self, text):
        """ Appends the provided text to the file.

        Parameters
        ----------
        text: str
            The text to append.

        Returns
        -------
        None
        """
        self._file_handler('append', text)

    def read_lines(self):
        """ Reads the lines of the file.

        Returns
        -------
        list
            The lines of the file.
        """
        return self._file_handler('read_lines')

    def write_lines(self, lines):
        """ Writes the provided lines to the file.

        Parameters
        ----------
        lines: str
            The lines to write.

        Returns
        -------
        None
        """
        self._file_handler('write_lines', lines)
