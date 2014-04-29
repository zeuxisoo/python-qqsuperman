# Python-QQSuperman

A RESET API wrapper for the QQSuperman

## Installation

Make sure you have python 2.7 and pip installed

Run command

    pip install qqsuperman

## Usage

Instance the object

    q = QQSuperman(username, password)

Get remainder point

    q.remainder_point()

Decode image

    q.decode_image('/path/to/image')

    > { 'code': 'nmvt', 'worker': '4D4EADF27E8645588F6C1447D87AFBB5' }

Report error

    q.report_error(worker_id)
