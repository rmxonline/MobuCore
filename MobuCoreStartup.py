'''
Startup script for adding the MobuCore menu to Motionbuilder on startup.

The full MobuCore package is required for this script.
________________________________________________________________________

This script was written by Dan Lowe as part of the MobuCore package. You can reach Dan Lowe on Twitter at https://twitter.com/danlowlows (at time of writing, direct messages are open).

MobuCore is made available under the following license terms:

Copyright (c) 2019 Dan Lowe

This software is provided 'as-is', without any express or implied warranty. In no event will the author be held liable for any damages arising from the use of this software.

Permission is granted to anyone to use this software for any purpose, including commercial applications, and to alter it and redistribute it freely, subject to the following restrictions:

1. The origin of this software must not be misrepresented; you must not claim that you wrote the original software.

2. If you use this software, in source or binary form, an acknowledgment in the product documentation or credits would be appreciated but is not required. Example: "This product uses MobuCore (c) 2019 Dan Lowe."

3. Altered source versions must be plainly marked as such, and must not be misrepresented as being the original software.

4. This notice may not be removed or altered from any source distribution.
'''

from MobuCore.MobuCoreMenu.MobuCoreMenu import LoadMenu

LoadMenu()