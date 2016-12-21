# -*- coding: utf-8 -*-
#
# Copyright 2012-2015 Spotify AB
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import datetime
import json
import random
import luigi
from luigi_tasks.senpy_analysis import SenpyTask

# class Elasticsearch(CopyToIndex):
#     """
#     This task loads JSON data contained in a :py:class:`luigi.target.Target` into an ElasticSearch index.
#     This task's input will the target returned by :py:meth:`~.Senpy.output`.
#     This class uses :py:meth:`luigi.contrib.esindex.CopyToIndex.run`.
#     After running this task you can run:
#     .. code-block:: console
#         $ curl "localhost:9200/example_index/_search?pretty"
#     to see the indexed documents.
#     To see the update log, run
#     .. code-block:: console
#         $ curl "localhost:9200/update_log/_search?q=target_index:example_index&pretty"
#     To cleanup both indexes run:
#     .. code-block:: console
#         $ curl -XDELETE "localhost:9200/example_index"
#         $ curl -XDELETE "localhost:9200/update_log/_query?q=target_index:example_index"
#     """
#
#     filename = luigi.Parameter()
#     analysis = luigi.Parameter()
#
#     #: date task parameter (default = today)
#     date = luigi.DateParameter(default=datetime.date.today())
#
#     #: the name of the index in ElasticSearch to be updated.
#     index = luigi.Parameter()
#
#     #: the name of the document type.
#     doc_type = luigi.Parameter()
#
#     #: the host running the ElasticSearch service.
#     host = 'localhost'
#
#     #: the port used by the ElasticSearch service.
#     port = 9200
#
#     def requires(self):
#         """
#         This task's dependencies:
#         * :py:class:`~.SenpyTask`
#         :return: object (:py:class:`luigi.task.Task`)
#         """
#         return SenpyTask(self.filename, self.analysis)

# class SemanticTask(luigi.Task):
#      """
#      This task loads JSON data contained in a :py:class:`luigi.target.Target` and transform into RDF file
#      to insert into Fuseki platform as a semantic
#      """
#      #: date task parameter (default = today)
#      date = luigi.DateParameter(default=datetime.date.today())
#      file = str(random.randint(0,10000)) + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
#
#      def output(self):
#         """
#         Returns the target output for this task.
#         In this case, a successful execution of this task will create a file on the local filesystem.
#         :return: the target output for this task.
#         :rtype: object (:py:class:`luigi.target.Target`)
#         """
#         return luigi.LocalTarget(path='/tmp/transformed-%s.n3' % self.file)
#
#
#      def requires(self):
#         """
#         This task's dependencies:
#         * :py:class:`~.SenpyTask`
#         :return: object (:py:class:`luigi.task.Task`)
#         """
#         return SenpyTask()
#
#      def run(self):
#         """
#         Receive data from Senpy and transform them to RDF format in order to be indexed in Fuseki
#         """
#         with self.input().open('r') as infile:
#             j = json.load(infile)
#             g = Graph().parse(data=j, format='json-ld')
#         with self.output().open('w') as output:
#             output.write(g.serialize(format='n3', indent=4))
    

if __name__ == "__main__":
    luigi.run()
