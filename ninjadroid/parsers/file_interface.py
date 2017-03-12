from abc import ABCMeta, abstractmethod


class FileInterface(metaclass=ABCMeta):
    """
    Parser interface for a file.
    """

    @staticmethod
    @abstractmethod
    def is_a_file(filepath):
        """
        Check whether a given path is a file.

        :param filepath: The path of the file to be checked.
        :return: True if the path is a file, False otherwise.
        """
        pass

    @staticmethod
    @abstractmethod
    def is_a_readable_file(filepath):
        """
        Check whether a given path is a readable file.

        :param filepath: The path of the file to be checked.
        :return: True if the file is readable, False otherwise.
        """
        pass

    @abstractmethod
    def dump(self):
        """
        Dump the File object into a Dictionary.

        :return: A Dictionary representing the File object.
        """
        pass

    @abstractmethod
    def get_raw_file(self):
        """
        Retrieve the raw file.

        :return: The raw file.
        """
        pass

    @abstractmethod
    def get_file_name(self):
        """
        Retrieve the file name.

        :return: The file name.
        """
        pass

    @abstractmethod
    def get_file_path(self):
        """
        Retrieve the file path.

        :return: The file path.
        """
        pass

    @abstractmethod
    def get_size(self):
        """
        Retrieve the size (in Bytes) of the file.

        :return: The size (in Bytes).
        """
        pass

    @abstractmethod
    def get_md5(self):
        """
        Retrieve the MD5 checksum of the file.

        :return: The MD5 checksum.
        """
        pass

    @abstractmethod
    def get_sha1(self):
        """
        Retrieve the SHA-1 checksum of the file.

        :return: The SHA-1 checksum.
        """
        pass

    @abstractmethod
    def get_sha256(self):
        """
        Retrieve the SHA-256 checksum of the file.

        :return: The SHA-256 checksum.
        """
        pass

    @abstractmethod
    def get_sha512(self):
        """
        Retrieve the SHA-512 checksum of the file.

        :return: The SHA-512 checksum.
        """
        pass
