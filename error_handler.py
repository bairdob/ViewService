import traceback

from flask import jsonify, request


def special_exception_handler(error):
    """
    Обработка любого необработанного исключения, для приведения в человекочитаемый вид.

    :param error: необработанная ошибка
    :type error: Exception
    :return: JSON данных ответа, код ответа
    :rtype: (str, int)
    """
    result = {
        'message': str(error),
        'traceback': traceback.format_exc(),
        'url': request.url,
    }

    # если это предсказуемая ошибка - там может быть статус ответа
    if hasattr(error, 'status'):
        status = error.status
    else:
        status = 500
    return jsonify(result), status
