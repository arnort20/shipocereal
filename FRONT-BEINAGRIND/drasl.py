def checkout_view(request):
    print('nanna')
    customer = request.user
    user_form = user_update_info.UpdateUserForm(instance=request.user)
    user_card = ship_o_cereal.models.Creditcards.objects.filter(userId=customer).first()
    user_address = ship_o_cereal.models.Addresses.objects.filter(userId=customer).first()
    if request.method == 'POST':
        print('if skipun')
        user_form = user_update_info.UpdateUserForm(instance=request.user)
        user_card_form = credit_card_form.CreditcardCreateForm(instance=user_card)
        user_address_form = address_form.AddressCreateForm(instance=user_address)


    user_form = user_update_info.UpdateUserForm(instance=request.user)
    user_card_form = credit_card_form.CreditcardCreateForm(instance=user_card)
    user_address_form = address_form.AddressCreateForm(instance=user_address)
    context = {'cart': ship_o_cereal.models.CartFolio.objects.filter(userId=customer),
            'user_address_form': user_address_form,
            'user_card_form': user_card_form,
            'user_form':user_form}
    return render(request, 'user/checkout_overview.html', context=context)
