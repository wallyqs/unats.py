# Copyright 2020 The NATS Authors
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
import unats as nats
import unittest

# TODO: Use mock for the socket

class ClientTest(unittest.TestCase):

    def test_simple_pub_single_sub(self):
        nc = nats.connect("localhost")
        sub = nc.subscribe("greet")

        nc.publish("greet", b'Hello World!')

        total = 0

        # NOTE: Once this is called, it would expect that any messages here
        # are of the same message. In case of having made other
        # subscriptions this will drop those messages.
        print()
        for msg in sub.next_msg():
            if total == 5:
                break
            print("Message:", msg)
            nc.publish("greet", b'Hello World!')
            total += 1

if __name__ == '__main__':
    unittest.main()
