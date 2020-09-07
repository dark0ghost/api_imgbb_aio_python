from typing import Any, Dict, Optional

import aiofiles
import aiohttp


class OutOfRange(Exception):
    pass


class ServiceError(Exception):
    pass


class ApiImgbb:
    last_json: Dict[str, Any]
    session: aiohttp.ClientSession

    def __init__(self, api_key: str, session: Optional[aiohttp.ClientSession] = None) -> None:
        """

        :param api_key:
        :param session:
        """
        self.last_json = dict()
        self.api_key: str = api_key
        if session is None:
            self.session = aiohttp.ClientSession()
            return
        self.session = session

    async def close(self) -> None:
        """

        :return:
        """
        await self.session.close()

    async def request(self, path_to_file: str, expiration: int = 600, name: Optional[str] = None) -> Dict[str, Any]:
        """
        image (required) A binary file, base64 data, or a URL for an image. (up to 32 MB)
        name (optional) The name of the file, this is automatically detected if uploading a file with a POST and multipart / form-data
        expiration (optional) Enable this if you want to force uploads to be auto deleted after certain time (in seconds 60-15552000)
        :param name:
        :param path_to_file:
        :param expiration:
        :return:
        """
        if not 60 <= expiration <= 15552000:
            raise OutOfRange("out of range 60 <= expiration <= 15552000")

        if name is None:
            link: str = f"https://api.imgbb.com/1/upload?expiration={expiration}&key={self.api_key}"
        else:
            link: str = f"https://api.imgbb.com/1/upload?expiration={expiration}&key={self.api_key}&name={name}"

        async with aiofiles.open(file=path_to_file, mode="rb") as file:
            async with self.session.post(url=link, data=file) as response:
                data: Dict[str, Any] = await response.json()
                if response.status == 200:
                    self.last_json = data
                    return data
                raise ServiceError(data['error']['message'])


