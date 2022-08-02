def get_days_count_by_month(month):
    """Возвращает количество дней по месяцу
    Args:
        month: название месяца
    Returns: количество дней
    """
    if month.capitalize() in ['Январь', 'Март', 'Май', 'Июль', 'Август', 'Октябрь', 'Декабрь']:
        print(31)
    elif month.capitalize() in ['Апрель', 'Июнь', 'Сентябрь', 'Ноябрь']:
        print(30)
    elif month.capitalize() =='Февраль':
        print(28)
    else:
        print(0)
    
    
    
    
    
    
    
    
    
    
