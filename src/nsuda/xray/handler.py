import asyncio
import uuid
import subprocess as sproc
from multiprocessing import Process
import json
import pathlib
import sys

class XrayHandler:
    @classmethod
    async def create(cls):
        '''
        1) Inits xray path by args\n
        2) Loads client config\n
        3) Loads server config\n
        '''
        self = cls()

        self._xray_path: str = sys.argv[1]
        self.cur_uuid: str = None
        self.server_config: str = None
        self.client_config: str = None
        self._xray_executor: Process = None

        await self._load_client_config()
        await self._load_server_config()

        return self
        
    async def update_uuid(self):
        async with asyncio.Lock():
            self.cur_uuid = str(uuid.uuid4())
            await self._update_config()
            self._reload_xray()
            

    async def _update_config(self):
        async with asyncio.Lock():
            # client config updating
            config_json = json.loads(self.client_config)
            config_json[
                "outbounds"
                ][0][
                    "settings"
                    ][
                        "vnext"
                        ][0][
                            "users"
                            ][0]["id"] = self.cur_uuid
            self.client_config = json.dumps(config_json)
            
            # server config updating
            config_json = json.loads(self.server_config)
            config_json[
                "inbounds"
                ][0][
                    "settings"
                    ][
                        "clients"
                        ][0]["id"] = self.cur_uuid
            self.server_config = json.dumps(config_json)

    async def _load_server_config(self):
        path = pathlib.Path(__file__).parent / "config/server_config.json"
        async with asyncio.Lock():
            with open(path, "r") as f:
                self.server_config = f.read()

    async def _load_client_config(self):
        path = pathlib.Path(__file__).parent / "config/client_config.json"
        async with asyncio.Lock():
            with open(path, "r") as f:
                self.client_config = f.read()

    def _execute(config, path):
        try:
            sproc.run(path.encode(), input=config.encode())
        except Exception as e:
            print(f"Xray have an error: {e}")

    def _reload_xray(self):
        if self._xray_executor:
            self._xray_executor.terminate()

        self._xray_executor = Process(
            group=None, kwargs={ "config": self.server_config,
                                "path": self._xray_path }, 
            target=XrayHandler._execute)
        self._xray_executor.start()
        


class HandlerBuilder:
    '''
    Provides singleton access to XrayHandler.
    '''
    _instanse: XrayHandler= None

    @staticmethod
    async def get_instanse():
        if not HandlerBuilder._instanse:
            HandlerBuilder._instanse = await XrayHandler.create()
        return HandlerBuilder._instanse