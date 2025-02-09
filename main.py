from xpandr import Xpandr
from buffer_manager import BufferManager

buffer_manager = BufferManager()
xpandr = Xpandr(buffer_manager)
xpandr.start()