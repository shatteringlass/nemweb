""" reading nemfiles and zipped nemfiles into pandas dataframes """

from io import BytesIO
from zipfile import ZipFile


class ZipFileStreamer(ZipFile):
    """ZipFile subclass, with method to extract ZipFile as byte stream to memory"""

    def __init__(self, filename):
        """Initialises ZipFile object, and adds member_count attribute"""
        ZipFile.__init__(self, filename)
        self.member_count = len(self.filelist)

    def extract_stream(self, member):
        """Extract a member from the archive as a byte stream or string steam, using
        its full name. 'member' may be a filename or a ZipInfo object. """
        return BytesIO(self.read(member))


class NEMFileReader:

    def __init__(self, nemfile_object):
        """
        Returns a dict containing a pandas dataframe each table in a nemfile.
        The fileobject needs to be unzipped csv (nemfile), and can be either a file or an
        an in stream fileobject.
        """
        table_dict = {}
        for line in nemfile_object.readlines():
            row = line.strip().decode().split(',')
            table = "{0}_{1}".format(row[1], row[2])


            #  new table
            if row[0] == "I":
                table_dict[table] = [row[4:]]
            
            #  append data to each table
            elif row[0] == "D":
                table_dict[table].append(row[4:])
        
        self.content = table_dict

    def get_content(self):
        return self.content


class NEMZipReader:

    def __init__(self, nemzip_object):
        """
        Returns a dict containing a pandas dataframe each table in a zipped nemfile.
        The fileobject is needs to be a zipped csv (nemzip), and can be either a file or an
        in stream fileobject.
        Function checks there is only one file to unzip, unzips to a nemfile (csv) in memory,
        and passes nemfile_object to nemfile reader.
        """
        with ZipFileStreamer(nemzip_object) as zipfile:
            if zipfile.member_count == 1:
                filename = zipfile.namelist()[0]
                nemfile_object = zipfile.extract_stream(filename)
                self.content = NEMFileReader(nemfile_object).get_content()
            else:
                raise Exception('More than one file in zipfile')

    def get_content(self):
        return self.content
