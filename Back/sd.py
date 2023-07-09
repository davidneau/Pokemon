"""
An example client that joins any rooms that its specified owner does.
"""
import showdown
from showdown import Room
import logging
from showdown.utils import strip_prefix

room_id_user = ""

#logging.basicConfig(level=logging.INFO)
#logger = logging.getLogger(__name__)


class FollowerClient(showdown.Client):
    def __init__(self, **kwargs):
        self.inc = 0
        self.room_id = ""
        self.log = []
        self.old_roomid = ""
        with open("./owner.txt", "rt") as o:
            ownername = o.read().strip()
        showdown.Client.__init__(self, **kwargs)
        self.owner = showdown.User(ownername, client=self)

    async def on_query_response(self, response_type, data):
        if response_type == "userdetails":
            try:
                print("rooms : ", list(data.get("rooms").keys())[-1][1:])
                self.room_id = list(data.get("rooms").keys())[-1][1:]
                await self.join(self.room_id)
            except:
                print("Aucune room trouvé")

    @showdown.Client.on_interval(interval=10)
    async def get_owner_details(self):
        await self.owner.request_user_details()

    async def on_receive(self, room_id, inp_type, params):
        #print(inp_type)
        #print(params)
        print("inp type :", inp_type)
        print("roomid ", room_id)
        print("self.room_id", self.room_id)
        if room_id != "" and len(params) != 0:
            print("append :", [inp_type, params])
            self.log.append([inp_type, params])
        if inp_type == "win":
            self.room_id = ""
            self.old_roomid = ""
        else:
            self.old_roomid = room_id