import luigi
import json


class FetchDataTask(luigi.Task):
    """
    Generates a local file containing 5 elements of data in JSON format.
    """
    filename = luigi.Parameter()
    analysis = luigi.Parameter()
    datatype = luigi.Parameter(default='tweet')

    def run(self):
        """
        Writes data in JSON format into the task's output target.
        The data objects have the following attributes:
        * `_id` is the default Elasticsearch id field,
        * `text`: the text,
        * `date`: the day when the data was created.
        """
        json_file = open("analysis/{0}".format(self.filename), 'r').read()
        json_list = [item for item in json_file.split('\n') if item.__len__() > 0]

        j = json.dumps(json_list)
        with self.output().open('w') as output:
            json.dump(j, output)
            output.write('\n')

    def output(self):
        """
        Returns the target output for this task.
        In this case, a successful execution of this task will create a file on the local filesystem.
        :return: the target output for this task.
        :rtype: object (:py:class:`luigi.target.Target`)
        """
        return luigi.LocalTarget(path='analysis/%s-fd' % self.filename)