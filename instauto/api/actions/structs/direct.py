from . import common as cmmn
import json
import logging

from typing import Optional, List

logger = logging.getLogger(__name__)


class _Base(cmmn.Base):
    broadcast_type: str

    def __init__(self, recipients: Optional[List[List[str]]], thread_ids: Optional[List[str]], *args, **kwargs):
        if recipients is not None:
            self.recipient_users = json.dumps(recipients)
            self.thread_ids = []
        elif thread_ids is not None:
            self.thread_ids = json.dumps(thread_ids)
            self.recipient_users = []
        else:
            raise ValueError("Neither `recipients` or `threads` are provided.")
        super().__init__(*args, **kwargs)
        self._exempt.extend(['endpoint', 'broadcast_type'])
    
    @property
    def endpoint(self):
        return f'direct_v2/threads/broadcast/{self.broadcast_type}/'


class Message(_Base):
    REQUEST = 'direct/message.json'
    broadcast_type = 'text'

    def __init__(self, message: str, recipients: Optional[List[List[str]]] = None,
                 threads: Optional[List[str]] = None, *args, **kwargs):
        self.text = message
        super().__init__(recipients, threads, *args, **kwargs)


class MediaShare(_Base):
    REQUEST = 'direct/mediashare.json'
    broadcast_type = 'media_share'

    def __init__(self, media_id: str, recipients: Optional[List[List[str]]] = None,
                 threads: Optional[List[str]] = None, *args, **kwargs):
        self.media_id = media_id
        super().__init__(recipients, threads, *args, **kwargs)


class LinkShare(_Base):
    REQUEST = 'direct/linkshare.json'
    broadcast_type = 'link'

    def __init__(self, text: str, links: List[str], recipients: Optional[List[List[str]]] = None,
                 threads: Optional[List[str]] = None, *args, **kwargs):
        if type(links) != list:
            links = [links]
        self.link_text = text
        self.link_urls = json.dumps(links)
        super().__init__(recipients, threads, *args, **kwargs)


class ProfileShare(_Base):
    REQUEST = 'direct/profileshare.json'
    broadcast_type = 'profile'

    def __init__(self, profile_id: str, recipients: Optional[List[List[str]]] = None,
                 threads: Optional[List[str]] = None, *args, **kwargs):
        self.profile_user_id = profile_id
        super().__init__(recipients, threads, *args, **kwargs)


class DirectPhoto(_Base):
    REQUEST = 'direct/photoshare.json'
    broadcast_type = 'configure_photo'

    def __init__(self, upload_id: str, recipients: Optional[List[List[str]]] = None,
                 threads: Optional[List[str]] = None, *args, **kwargs):
        self.upload_id = upload_id
        self.allow_full_aspect_ratio = True
        super().__init__(recipients, threads, *args, **kwargs)


class DirectVideo(_Base):
    REQUEST = 'direct/videoshare.json'
    broadcast_type = 'configure_video'
    sampled = True
    video_result = ''

    def __init__(self, upload_id: str, recipients: Optional[List[List[str]]] = None,
                 threads: Optional[List[str]] = None, *args, **kwargs):
        self.upload_id = upload_id
        self.sampled = True
        self.video_result = ''
        super().__init__(recipients, threads, *args, **kwargs)


class DirectThread(cmmn.Base):
    thread_id: str

    def __init__(self, thread_id: str, *args, **kwargs):
        self.thread_id = thread_id
        super().__init__(*args, **kwargs)
