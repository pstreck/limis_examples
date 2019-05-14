from limis.services import Service

from hello.components import HelloComponent


services = [
    Service(name='hello', path='hello', components=[HelloComponent]),
]
