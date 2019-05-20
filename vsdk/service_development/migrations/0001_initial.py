# Generated by Django 2.0.4 on 2019-05-20 16:25

from django.db import migrations, models
import django.db.models.deletion
import vsdk.service_development.models.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(auto_now_add=True, verbose_name='Starting time')),
                ('end', models.DateTimeField(blank=True, null=True, verbose_name='Ending time')),
                ('caller_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='Caller ID')),
            ],
            options={
                'verbose_name': 'Call Session',
            },
        ),
        migrations.CreateModel(
            name='CallSessionStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='Time')),
                ('description', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Description')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='service_development.CallSession')),
            ],
            options={
                'verbose_name': 'Call Session Step',
            },
        ),
        migrations.CreateModel(
            name='KasaDakaUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caller_id', models.CharField(max_length=100, unique=True, verbose_name='Phone number')),
                ('first_name', models.CharField(blank=True, max_length=100, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=100, verbose_name='Last name')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='Date last modified')),
            ],
            options={
                'verbose_name': 'KasaDaka User',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='Code')),
            ],
            options={
                'verbose_name': 'Language',
            },
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('startdate', models.DateField(auto_now_add=True)),
                ('enddate', models.DateField()),
            ],
            options={
                'verbose_name': 'Offer Element',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Product Element',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Region Element',
            },
        ),
        migrations.CreateModel(
            name='SpokenUserInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio', models.FileField(upload_to='uploads/', verbose_name='Audio file')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='Time')),
                ('description', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Spoken User Input',
            },
        ),
        migrations.CreateModel(
            name='UserInputCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'User Input Category',
            },
        ),
        migrations.CreateModel(
            name='VoiceFragment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio', models.FileField(help_text='Ensure your file is in the correct format! Wave (.wav) : Sample rate 8KHz, 16 bit, mono, Codec: PCM 16 LE (s16l)', upload_to='', validators=[vsdk.service_development.models.validators.validate_audio_file_extension], verbose_name='Audio')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service_development.Language')),
            ],
            options={
                'verbose_name': 'Voice Fragment',
            },
        ),
        migrations.CreateModel(
            name='VoiceLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Voice Label',
            },
        ),
        migrations.CreateModel(
            name='VoiceService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.CharField(max_length=1000, verbose_name='Description')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='Date last modified')),
                ('active', models.BooleanField(help_text='A voice service that is active is accessible to users. Marking this service as active (which is only possible when it is valid) will activate this service and disactivate all other services.', verbose_name='Voice service active')),
                ('registration', models.CharField(choices=[('required', 'required (service does not function without Caller ID!)'), ('preferred', 'preferred'), ('disabled', 'disabled')], max_length=15, verbose_name='User registration')),
                ('registration_language', models.BooleanField(default=True, help_text='The preferred language will be asked and stored during the user registration process', verbose_name='Register Language preference')),
                ('registration_name', models.BooleanField(default=False, help_text='The user will be asked to speak their name as part of the user registration process', verbose_name='Register spoken name')),
                ('supported_languages', models.ManyToManyField(blank=True, to='service_development.Language', verbose_name='Supported languages')),
            ],
            options={
                'verbose_name': 'Voice Service',
            },
        ),
        migrations.CreateModel(
            name='VoiceServiceSubElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('modification_date', models.DateTimeField(auto_now=True, verbose_name='Date last modified')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.CharField(blank=True, max_length=1000)),
            ],
            options={
                'verbose_name': 'Voice Service Sub-Element',
            },
        ),
        migrations.CreateModel(
            name='ChoiceOption',
            fields=[
                ('voiceservicesubelement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='service_development.VoiceServiceSubElement')),
            ],
            options={
                'verbose_name': 'Voice Service',
            },
            bases=('service_development.voiceservicesubelement',),
        ),
        migrations.CreateModel(
            name='VoiceServiceElement',
            fields=[
                ('voiceservicesubelement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='service_development.VoiceServiceSubElement')),
            ],
            options={
                'verbose_name': 'Voice Service Element',
            },
            bases=('service_development.voiceservicesubelement',),
        ),
        migrations.AddField(
            model_name='voiceservicesubelement',
            name='service',
            field=models.ForeignKey(help_text='The service to which this element belongs', on_delete=django.db.models.deletion.CASCADE, to='service_development.VoiceService'),
        ),
        migrations.AddField(
            model_name='voiceservicesubelement',
            name='voice_label',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='service_development.VoiceLabel', verbose_name='Voice label'),
        ),
        migrations.AddField(
            model_name='voicefragment',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service_development.VoiceLabel'),
        ),
        migrations.AddField(
            model_name='userinputcategory',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service', to='service_development.VoiceService', verbose_name='Voice service'),
        ),
        migrations.AddField(
            model_name='spokenuserinput',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='service_development.UserInputCategory', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='spokenuserinput',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='session', to='service_development.CallSession'),
        ),
        migrations.AddField(
            model_name='region',
            name='voice_label',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='service_development.VoiceLabel', verbose_name='Voice label'),
        ),
        migrations.AddField(
            model_name='product',
            name='voice_label',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='service_development.VoiceLabel', verbose_name='Voice label'),
        ),
        migrations.AddField(
            model_name='offer',
            name='product_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='service_development.Product', verbose_name='Product type'),
        ),
        migrations.AddField(
            model_name='offer',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='service_development.Region', verbose_name='Region'),
        ),
        migrations.AddField(
            model_name='offer',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service_development.KasaDakaUser', verbose_name='Caller id'),
        ),
        migrations.AddField(
            model_name='offer',
            name='voice_label',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='service_development.VoiceLabel', verbose_name='Voice label'),
        ),
        migrations.AddField(
            model_name='language',
            name='eight',
            field=models.ForeignKey(help_text='The number 8', on_delete=django.db.models.deletion.PROTECT, related_name='language_eight', to='service_development.VoiceLabel', verbose_name='The number 8'),
        ),
        migrations.AddField(
            model_name='language',
            name='error_message',
            field=models.ForeignKey(help_text='A general error message', on_delete=django.db.models.deletion.PROTECT, related_name='language_error_message', to='service_development.VoiceLabel', verbose_name='Error message voice label'),
        ),
        migrations.AddField(
            model_name='language',
            name='five',
            field=models.ForeignKey(help_text='The number 5', on_delete=django.db.models.deletion.PROTECT, related_name='language_five', to='service_development.VoiceLabel', verbose_name='The number 5'),
        ),
        migrations.AddField(
            model_name='language',
            name='four',
            field=models.ForeignKey(help_text='The number 4', on_delete=django.db.models.deletion.PROTECT, related_name='language_four', to='service_development.VoiceLabel', verbose_name='The number 4'),
        ),
        migrations.AddField(
            model_name='language',
            name='nine',
            field=models.ForeignKey(help_text='The number 9', on_delete=django.db.models.deletion.PROTECT, related_name='language_nine', to='service_development.VoiceLabel', verbose_name='The number 9'),
        ),
        migrations.AddField(
            model_name='language',
            name='one',
            field=models.ForeignKey(help_text='The number 1', on_delete=django.db.models.deletion.PROTECT, related_name='language_one', to='service_development.VoiceLabel', verbose_name='The number 1'),
        ),
        migrations.AddField(
            model_name='language',
            name='post_choice_option',
            field=models.ForeignKey(help_text="The fragment that is to be played before a choice option (e.g. 'to select option X, [please press] 1')", on_delete=django.db.models.deletion.PROTECT, related_name='language_post_choice_option', to='service_development.VoiceLabel', verbose_name='Post-Choice Option voice label'),
        ),
        migrations.AddField(
            model_name='language',
            name='pre_choice_option',
            field=models.ForeignKey(help_text="The fragment that is to be played before a choice option (e.g. '[to select] option X, please press 1')", on_delete=django.db.models.deletion.PROTECT, related_name='language_pre_choice_option', to='service_development.VoiceLabel', verbose_name='Pre-Choice Option voice label'),
        ),
        migrations.AddField(
            model_name='language',
            name='select_language',
            field=models.ForeignKey(help_text='A message requesting the user to select a language', on_delete=django.db.models.deletion.PROTECT, related_name='language_select_language', to='service_development.VoiceLabel', verbose_name='Select language voice label'),
        ),
        migrations.AddField(
            model_name='language',
            name='seven',
            field=models.ForeignKey(help_text='The number 7', on_delete=django.db.models.deletion.PROTECT, related_name='language_seven', to='service_development.VoiceLabel', verbose_name='The number 7'),
        ),
        migrations.AddField(
            model_name='language',
            name='six',
            field=models.ForeignKey(help_text='The number 6', on_delete=django.db.models.deletion.PROTECT, related_name='language_six', to='service_development.VoiceLabel', verbose_name='The number 6'),
        ),
        migrations.AddField(
            model_name='language',
            name='three',
            field=models.ForeignKey(help_text='The number 3', on_delete=django.db.models.deletion.PROTECT, related_name='language_three', to='service_development.VoiceLabel', verbose_name='The number 3'),
        ),
        migrations.AddField(
            model_name='language',
            name='two',
            field=models.ForeignKey(help_text='The number 2', on_delete=django.db.models.deletion.PROTECT, related_name='language_two', to='service_development.VoiceLabel', verbose_name='The number 2'),
        ),
        migrations.AddField(
            model_name='language',
            name='voice_label',
            field=models.ForeignKey(help_text='A Voice Label of the name of the language', on_delete=django.db.models.deletion.PROTECT, related_name='language_description_voice_label', to='service_development.VoiceLabel', verbose_name='Language voice label'),
        ),
        migrations.AddField(
            model_name='language',
            name='zero',
            field=models.ForeignKey(help_text='The number 0', on_delete=django.db.models.deletion.PROTECT, related_name='language_zero', to='service_development.VoiceLabel', verbose_name='The number 0'),
        ),
        migrations.AddField(
            model_name='kasadakauser',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='service_development.Language'),
        ),
        migrations.AddField(
            model_name='kasadakauser',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service_development.VoiceService'),
        ),
        migrations.AddField(
            model_name='callsession',
            name='_language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='service_development.Language'),
        ),
        migrations.AddField(
            model_name='callsession',
            name='_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='service_development.Product'),
        ),
        migrations.AddField(
            model_name='callsession',
            name='_region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='service_development.Region'),
        ),
        migrations.AddField(
            model_name='callsession',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='service_development.VoiceService'),
        ),
        migrations.AddField(
            model_name='callsession',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='service_development.KasaDakaUser'),
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('voiceserviceelement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='service_development.VoiceServiceElement')),
            ],
            options={
                'verbose_name': 'Choice Element',
            },
            bases=('service_development.voiceserviceelement',),
        ),
        migrations.CreateModel(
            name='MessagePresentation',
            fields=[
                ('voiceserviceelement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='service_development.VoiceServiceElement')),
                ('final_element', models.BooleanField(default=False, verbose_name='This element will terminate the call')),
            ],
            options={
                'verbose_name': 'Message Presentation Element',
            },
            bases=('service_development.voiceserviceelement',),
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('voiceserviceelement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='service_development.VoiceServiceElement')),
                ('repeat_recording_to_caller', models.BooleanField(default=True, verbose_name='Repeat the recording to the caller before asking for confirmation')),
                ('ask_confirmation', models.BooleanField(default=True, verbose_name='Ask the caller to confirm their recording')),
                ('max_time_input', models.IntegerField(default=180, verbose_name='Maximum time of message (seconds)')),
            ],
            options={
                'verbose_name': 'Spoken Input Element',
            },
            bases=('service_development.voiceserviceelement',),
        ),
        migrations.CreateModel(
            name='Vse_Own_Added',
            fields=[
                ('voiceserviceelement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='service_development.VoiceServiceElement')),
                ('final_element', models.BooleanField(default=False, verbose_name='This element will terminate the call')),
                ('_redirect', models.ForeignKey(blank=True, help_text='The element to redirect to after the message has been played.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='service_development_vse_own_added_related', to='service_development.VoiceServiceElement', verbose_name='Redirect element')),
            ],
            options={
                'verbose_name': 'Own Added Elements',
            },
            bases=('service_development.voiceserviceelement',),
        ),
        migrations.AddField(
            model_name='voiceservice',
            name='_start_element',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='service_development_voiceservice_related', to='service_development.VoiceServiceElement', verbose_name='Starting element'),
        ),
        migrations.AddField(
            model_name='choiceoption',
            name='_redirect',
            field=models.ForeignKey(blank=True, help_text='The element to redirect to when this choice is made by the user.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='service_development_choiceoption_redirect_related', to='service_development.VoiceServiceElement', verbose_name='Redirect element'),
        ),
        migrations.AddField(
            model_name='callsessionstep',
            name='_visited_element',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='service_development.VoiceServiceElement'),
        ),
        migrations.AddField(
            model_name='record',
            name='_redirect',
            field=models.ForeignKey(blank=True, help_text='The element to redirect to after the message has been played.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='service_development_record_related', to='service_development.VoiceServiceElement', verbose_name='Redirect element'),
        ),
        migrations.AddField(
            model_name='record',
            name='ask_confirmation_voice_label',
            field=models.ForeignKey(blank=True, help_text='The voice label that asks the user to confirm their pinput. Example: "Are you satisfied with your recording? Press 1 to confirm, or press 2 to retry."', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='confirmation_voice_label', to='service_development.VoiceLabel', verbose_name='Ask for confirmation voice label'),
        ),
        migrations.AddField(
            model_name='record',
            name='final_voice_label',
            field=models.ForeignKey(blank=True, help_text='The voice label that is played when the user has completed the recording process. Example: "Thank you for your message! The message has been stored successfully."', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='final_voice_label', to='service_development.VoiceLabel', verbose_name='Final voice label'),
        ),
        migrations.AddField(
            model_name='record',
            name='input_category',
            field=models.ForeignKey(blank=True, help_text='The category under which the input will be stored in the system.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='input_category', to='service_development.UserInputCategory', verbose_name='Input category'),
        ),
        migrations.AddField(
            model_name='record',
            name='not_heard_voice_label',
            field=models.ForeignKey(blank=True, help_text='The voice label that is played when the system does not recognize the user saying anything. Example: "We did not hear anything, please speak your message."', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='not_heard_voice_label', to='service_development.VoiceLabel', verbose_name='No response voice label'),
        ),
        migrations.AddField(
            model_name='record',
            name='repeat_voice_label',
            field=models.ForeignKey(blank=True, help_text='The voice label that is played before the system repeats the user input. Example: "Your message is:"', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='repeat_voice_label', to='service_development.VoiceLabel', verbose_name='Repeat input voice label'),
        ),
        migrations.AddField(
            model_name='messagepresentation',
            name='_redirect',
            field=models.ForeignKey(blank=True, help_text='The element to redirect to after the message has been played.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='service_development_messagepresentation_related', to='service_development.VoiceServiceElement', verbose_name='Redirect element'),
        ),
        migrations.AddField(
            model_name='choiceoption',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice_options', to='service_development.Choice'),
        ),
    ]
