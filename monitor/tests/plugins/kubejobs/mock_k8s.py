# Copyright (c) 2017 UFCG-LSD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

class Job():

    def __init__(self, active):

        self.status = Status(active)

class Status():

    def __init__(self, active):

        self.active = active

class MockKube():

    def __init__(self, app_id, replicas=1, namespace="default"):
        
        self.jobs = {namespace: {app_id: replicas}}
        
    def read_namespaced_job(self, name, namespace):

        out = Job(self.jobs[namespace][name])
        return out