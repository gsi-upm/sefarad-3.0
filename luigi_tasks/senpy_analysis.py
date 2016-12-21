import json
import luigi
import requests
from luigi_tasks.fetch_data_from_json import FetchDataTask


class SenpyTask(luigi.Task):
    """
    This task loads data fetched with previous task and send it to Senpy tool in order to analyze
    data retrieved and check sentiments expressed.
    """
    filename = luigi.Parameter()
    analysis = luigi.Parameter(default='sentiments')
    datatype = luigi.Parameter(default='tweet')

    def requires(self):
        """
        This task's dependencies:
        * :py:class:`~.FetchDataTask`
        :return: object (:py:class:`luigi.task.Task`)
        """
        return FetchDataTask(self.filename, self.analysis)

    def output(self):
        """
        Returns the target output for this task.
        In this case, a successful execution of this task will create a file on the local filesystem.
        :return: the target output for this task.
        :rtype: object (:py:class:`luigi.target.Target`)
        """
        return luigi.LocalTarget(path='analysis/%s-pp' % self.filename)

    def run_twitter(self, json_serialized):
        json_deserialized = self.deserialize_list(json_serialized)
        if self.analysis == 'sentiments':
            for tweet in json_deserialized:
                r = requests.get('http://senpy.cluster.gsi.dit.upm.es/api/?algo=sentiText&i=%s' % tweet["text"])
                response = r.content.decode('utf-8')
                response_json = json.loads(response)
                tweet["sentimentAnalysis"] = response_json
            return json_deserialized

        elif self.analysis == 'emotions':
            for tweet in json_deserialized:
                r = requests.get('http://senpy.cluster.gsi.dit.upm.es/api/?algo=EmoText&i=%s' % tweet["text"])
                response = r.content.decode('utf-8')
                response_json = json.loads(response)

                tweet["emotionAnalysis"] = response_json
            return json_deserialized

    def run(self):
        """
        Send data to Senpy tool and retrieve it analyzed. Store data in a json file.
        """
        with self.output().open('w') as output:
            with self.input().open('r') as infile:
                json_serialized = json.load(infile)
                senpy_data = 'No data was found!'
                if self.datatype == 'tweet':
                    senpy_data = self.run_twitter(json_serialized)

                output.write(json.dumps(senpy_data))
                output.write('\n')

    @staticmethod
    def tweets_filtering(tweet_raw):
        return {
            'text': tweet_raw['text'],
            'hashtags': tweet_raw['hashtags'],
            'mentions': tweet_raw['user_mentions'],
            'id': tweet_raw['id']
        }

    @staticmethod
    def deserialize_list(data):
        return [json.loads(item) for item in json.loads(data)]
