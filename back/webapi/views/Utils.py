from webapi.CrontabManager import CrontabManager


def add_job_in_crontab(alarm):
    """
    use the crontab manager to add a new job
    :param alarm: AlarmClock
    :return:
    """
    day_of_week = _get_day_of_week(alarm)
    new_job = "%s %s * * %s echo test # piclodio%s" % (alarm.minute, alarm.hour, day_of_week, alarm.id)
    if not alarm.is_active:
        line = "# "
        new_job = line + new_job
    print new_job
    CrontabManager.add_job(new_job)


def _get_day_of_week(alarm):
    """
    get a valid day of week period string usable with crontab
    :param alarm: AlarmClock
    :type alarm: AlarmClock
    :return:
    """

    def add_el(current_string, el):
        if current_string is not None:
            el = ",%s" % el
            current_string += el
        else:
            current_string = el
        return current_string

    returned_period = None
    if alarm.sunday:
        returned_period = add_el(returned_period, "0")
    if alarm.monday:
        returned_period = add_el(returned_period, "1")
    if alarm.tuesday:
        returned_period = add_el(returned_period, "2")
    if alarm.wednesday:
        returned_period = add_el(returned_period, "3")
    if alarm.thursday:
        returned_period = add_el(returned_period, "4")
    if alarm.friday:
        returned_period = add_el(returned_period, "5")
    if alarm.saturday:
        returned_period = add_el(returned_period, "6")

    return returned_period
