from django.dispatch import receiver
from django.db.models.signals import pre_delete

from restapi.models import AlarmClock


@receiver(pre_delete, sender=AlarmClock)
def delete_alarm_clock_callback(sender, **kwargs):
    """
    signals used to delete automatically an alarm from the scheduler
    """
    print("Signals delete alarm clock triggered")
    from utils.scheduler_manager import SchedulerManager
    scheduler_manager = SchedulerManager()
    scheduler_manager.delete_job_by_id(kwargs['instance'].id)
