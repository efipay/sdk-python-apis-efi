# encoding: utf-8

class Constants(object):
    APIS = {
        'CHARGES': {
            'URL': {
                'production': 'https://cobrancas.api.efipay.com.br/v1',
                'sandbox': 'https://cobrancas-h.api.efipay.com.br/v1'
            },
            'ENDPOINTS': {
                'authorize': {
                    'route': '/authorize',
                    'method': 'post'
                },
                'create_charge': {
                    'route': '/charge',
                    'method': 'post'
                },
                'create_one_step_charge': {
                    'route': '/charge/one-step',
                    'method': 'post'
                },
                'detail_charge': {
                    'route': '/charge/:id',
                    'method': 'get'
                },
                'update_charge_metadata': {
                    'route': '/charge/:id/metadata',
                    'method': 'put'
                },
                'update_billet': {
                    'route': '/charge/:id/billet',
                    'method': 'put'
                },
                'define_pay_method': {
                    'route': '/charge/:id/pay',
                    'method': 'post'
                },
                'cancel_charge': {
                    'route': '/charge/:id/cancel',
                    'method': 'put'
                },
                'create_carnet': {
                    'route': '/carnet',
                    'method': 'post'
                },
                'detail_carnet': {
                    'route': '/carnet/:id',
                    'method': 'get'
                },
                'update_carnet_parcel': {
                    'route': '/carnet/:id/parcel/:parcel',
                    'method': 'put'
                },
                'update_carnet_metadata': {
                    'route': '/carnet/:id/metadata',
                    'method': 'put'
                },
                'get_notification': {
                    'route': '/notification/:token',
                    'method': 'get'
                },
                'list_plans': {
                    'route': '/plans',
                    'method': 'get'
                },
                'create_plan': {
                    'route': '/plan',
                    'method': 'post'
                },
                'delete_plan': {
                    'route': '/plan/:id',
                    'method': 'delete'
                },
                'create_subscription': {
                    'route': '/plan/:id/subscription',
                    'method': 'post'
                },
                'create_one_step_subscription': {
                    'route': '/plan/:id/subscription/one-step',
                    'method': 'post'
                },
                'create_one_step_subscription_link': {
                    'route': '/plan/:id/subscription/one-step/link',
                    'method': 'post'
                },
                'detail_subscription': {
                    'route': '/subscription/:id',
                    'method': 'get'
                },
                'define_subscription_pay_method': {
                    'route': '/subscription/:id/pay',
                    'method': 'post'
                },
                'cancel_subscription': {
                    'route': '/subscription/:id/cancel',
                    'method': 'put'
                },
                'update_subscription_metadata': {
                    'route': '/subscription/:id/metadata',
                    'method': 'put'
                },
                'update_subscription': {
                    'route': '/subscription/:id',
                    'method': 'put'
                },
                'create_subscription_history': {
                    'route': '/subscription/:id/history',
                    'method': 'post'
                },
                'send_subscription_link_email': {
                    'route': '/charge/:id/subscription/resend',
                    'method': 'post'
                },
                'get_installments': {
                    'route': '/installments',
                    'method': 'get'
                },
                'send_billet_email': {
                    'route': '/charge/:id/billet/resend',
                    'method': 'post'
                },
                'create_charge_history': {
                    'route': '/charge/:id/history',
                    'method': 'post'
                },
                'send_carnet_email': {
                    'route': '/carnet/:id/resend',
                    'method': 'post'
                },
                'send_carnet_parcel_email': {
                    'route': '/carnet/:id/parcel/:parcel/resend',
                    'method': 'post'
                },
                'create_carnet_history': {
                    'route': '/carnet/:id/history',
                    'method': 'post'
                },
                'cancel_carnet': {
                    'route': '/carnet/:id/cancel',
                    'method': 'put'
                },
                'cancel_carnet_parcel': {
                    'route': '/carnet/:id/parcel/:parcel/cancel',
                    'method': 'put'
                },
                'create_one_step_link': {
                    'route': '/charge/one-step/link',
                    'method': 'post'
                },
                'define_link_pay_method': {
                    'route': '/charge/:id/link',
                    'method': 'post'
                },
                'update_charge_link': {
                    'route': '/charge/:id/link',
                    'method': 'put'
                },
                'send_link_email': {
                    'route': '/charge/:id/link/resend',
                    'method': 'post'
                },
                'update_plan': {
                    'route': '/plan/:id',
                    'method': 'put'
                },
                'define_balance_sheet_billet': {
                    'route': '/charge/:id/balance-sheet',
                    'method': 'post'
                },
                'settle_charge': {
                    'route': '/charge/:id/settle',
                    'method': 'put'
                },
                'settle_carnet': {
                    'route': '/carnet/:id/settle',
                    'method': 'put'
                },
                'settle_carnet_parcel': {
                    'route': '/carnet/:id/parcel/:parcel/settle',
                    'method': 'put'
                },
                'card_payment_retry': {
                    'route': '/charge/:id/retry',
                    'method': 'post'
                },
                'refund_card': {
                    'route': '/charge/card/:id/refund',
                    'method': 'post'
                },
                'update_carnet_parcels': {
                    'route': '/carnet/:id/parcels',
                    'method': 'put'
                },
                'list_charges': {
                    'route': '/charges',
                    'method': 'get'
                }
            }
        },
        'PIX': {
            'URL': {
                'production': 'https://pix.api.efipay.com.br',
                'sandbox': 'https://pix-h.api.efipay.com.br'
            },
            'ENDPOINTS': {
                'authorize': {
                    'route': '/oauth/token',
                    'method': 'post'
                },
                'pix_config_webhook': {
                    'route': '/v2/webhook/:chave',
                    'method': 'put'
                },
                'pix_detail_webhook': {
                    'route': '/v2/webhook/:chave',
                    'method': 'get'
                },
                'pix_list_webhook': {
                    'route': '/v2/webhook',
                    'method': 'get'
                },
                'pix_delete_webhook': {
                    'route': '/v2/webhook/:chave',
                    'method': 'delete'
                },
                'pix_resend_webhook': {
                    'route': '/v2/gn/webhook/reenviar',
                    'method': 'post'
                },
                'pix_create_charge': {
                    'route': '/v2/cob/:txid',
                    'method': 'put'
                },
                'pix_create_immediate_charge': {
                    'route': '/v2/cob',
                    'method': 'post'
                },
                'pix_detail_charge': {
                    'route': '/v2/cob/:txid',
                    'method': 'get'
                },
                'pix_update_charge': {
                    'route': '/v2/cob/:txid',
                    'method': 'patch'
                },
                'pix_list_charges': {
                    'route': '/v2/cob',
                    'method': 'get'
                },
                'pix_generate_qrcode': {
                    'route': '/v2/loc/:id/qrcode',
                    'method': 'get'
                },
                'pix_devolution': {
                    'route': '/v2/pix/:e2eId/devolucao/:id',
                    'method': 'put'
                },
                'pix_detail_devolution': {
                    'route': '/v2/pix/:e2eId/devolucao/:id',
                    'method': 'get'
                },
                'pix_send': {
                    'route': '/v2/gn/pix/:idEnvio',
                    'method': 'put'
                },
                'pix_send_detail': {
                    'route': '/v2/gn/pix/enviados/:e2eid',
                    'method': 'get'
                },
                'pix_send_list': {
                    'route': '/v2/gn/pix/enviados',
                    'method': 'get'
                },
                'pix_detail_received': {
                    'route': '/v2/pix/:e2eId',
                    'method': 'get'
                },
                'pix_received_list': {
                    'route': '/v2/pix',
                    'method': 'get'
                },
                'pix_list_received': {
                    'route': '/v2/pix',
                    'method': 'get'
                },
                'pix_create_location': {
                    'route': '/v2/loc',
                    'method': 'post'
                },
                'pix_location_list': {
                    'route': '/v2/loc',
                    'method': 'get'
                },
                'pix_detail_location': {
                    'route': '/v2/loc/:id',
                    'method': 'get'
                },
                'pix_unlink_txid_location': {
                    'route': '/v2/loc/:id/txid',
                    'method': 'delete'
                },
                'pix_create_evp': {
                    'route': '/v2/gn/evp',
                    'method': 'post'
                },
                'pix_list_evp': {
                    'route': '/v2/gn/evp',
                    'method': 'get'
                },
                'pix_delete_evp': {
                    'route': '/v2/gn/evp/:chave',
                    'method': 'delete'
                },
                'get_account_balance': {
                    'route': '/v2/gn/saldo',
                    'method': 'get'
                },
                'update_account_config': {
                    'route': '/v2/gn/config',
                    'method': 'put'
                },
                'list_account_config': {
                    'route': '/v2/gn/config',
                    'method': 'get'
                },
                'pix_create_due_charge': {
                    'route': '/v2/cobv/:txid',
                    'method': 'put'
                },
                'pix_update_due_charge': {
                    'route': '/v2/cobv/:txid',
                    'method': 'patch'
                },
                'pix_detail_due_charge': {
                    'route': '/v2/cobv/:txid',
                    'method': 'get'
                },
                'pix_list_due_charges': {
                    'route': '/v2/cobv/',
                    'method': 'get'
                },
                'create_report': {
                    'route': '/v2/gn/relatorios/extrato-conciliacao',
                    'method': 'post'
                },
                'detail_report': {
                    'route': '/v2/gn/relatorios/:id',
                    'method': 'get'
                },
                'pix_split_detail_charge': {
                    'route': '/v2/gn/split/cob/:txid',
                    'method': 'get'
                },
                'pix_split_link_charge': {
                    'route': '/v2/gn/split/cob/:txid/vinculo/:splitConfigId',
                    'method': 'put'
                },
                'pix_split_unlink_charge': {
                    'route': '/v2/gn/split/cob/:txid/vinculo',
                    'method': 'delete'
                },
                'pix_split_detail_due_charge': {
                    'route': '/v2/gn/split/cobv/:txid',
                    'method': 'get'
                },
                'pix_split_link_due_charge': {
                    'route': '/v2/gn/split/cobv/:txid/vinculo/:splitConfigId',
                    'method': 'put'
                },
                'pix_split_unlink_due_charge': {
                    'route': '/v2/gn/split/cobv/:txid/vinculo',
                    'method': 'delete'
                },
                'pix_split_config_id': {
                    'route': '/v2/gn/split/config/:id',
                    'method': 'put'
                },
                'pix_split_config': {
                    'route': '/v2/gn/split/config',
                    'method': 'post'
                },
                'pix_split_detail_config': {
                    'route': '/v2/gn/split/config/:id',
                    'method': 'get'
                },
                'pix_send_detail_id': {
                    'route': '/v2/gn/pix/enviados/id-envio/:idEnvio',
                    'method': 'get'
                },
                'med_list': {
                    'route': '/v2/gn/infracoes',
                    'method': 'get'
                },
                'med_defense': {
                    'route': '/v2/gn/infracoes/:idInfracao/defesa',
                    'method': 'post'
                },
                'pix_create_due_charge_batch': {
                    'route': '/v2/lotecobv/:id',
                    'method': 'put'
                },
                'pix_update_due_charge_batch': {
                    'route': '/v2/lotecobv/:id',
                    'method': 'patch'
                },
                'pix_detail_due_charge_batch': {
                    'route': '/v2/lotecobv/:id',
                    'method': 'get'
                },
                'pix_list_due_charge_batch': {
                    'route': '/v2/lotecobv',
                    'method': 'get'
                },
                'pix_qrcode_pay': {
                    'route': '/v2/gn/pix/:idEnvio/qrcode',
                    'method': 'put'
                },
                'pix_qrcode_detail': {
                    'route': '/v2/gn/qrcodes/detalhar',
                    'method': 'post'
                },
                'pix_get_receipt': {
                    'route': '/v2/gn/pix/comprovantes',
                    'method': 'get'
                },
                'pix_detail_recurrence_automatic': {
                    'route': '/v2/rec/:idRec',
                    'method': 'get'
                },
                'pix_update_recurrence_automatic': {
                    'route': '/v2/rec/:idRec',
                    'method': 'patch'
                },
                'pix_list_recurrence_automatic': {
                    'route': '/v2/rec',
                    'method': 'get'
                },
                'pix_create_recurrence_automatic': {
                    'route': '/v2/rec',
                    'method': 'post'
                },
                'pix_create_request_recurrence_automatic': {
                    'route': '/v2/solicrec',
                    'method': 'post'
                },
                'pix_detail_request_recurrence_automatic': {
                    'route': '/v2/solicrec/:idSolicRec',
                    'method': 'get'
                },
                'pix_update_request_recurrence_automatic': {
                    'route': '/v2/solicrec/:idSolicRec',
                    'method': 'patch'
                },
                'pix_create_automatic_charge_txid': {
                    'route': '/v2/cobr/:txid',
                    'method': 'put'
                },
                'pix_update_automatic_charge': {
                    'route': '/v2/cobr/:txid',
                    'method': 'patch'
                },
                'pix_detail_automatic_charge': {
                    'route': '/v2/cobr/:txid',
                    'method': 'get'
                },
                'pix_create_automatic_charge': {
                    'route': '/v2/cobr',
                    'method': 'post'
                },
                'pix_list_automatic_charge': {
                    'route': '/v2/cobr',
                    'method': 'get'
                },
                'pix_retry_request_automatic': {
                    'route': '/v2/cobr/:txid/retentativa/:data',
                    'method': 'post'
                },
                'pix_create_location_recurrence_automatic': {
                    'route': '/v2/locrec',
                    'method': 'post'
                },
                'pix_list_location_recurrence_automatic': {
                    'route': '/v2/locrec',
                    'method': 'get'
                },
                'pix_detail_location_recurrence_automatic': {
                    'route': '/v2/locrec/:id',
                    'method': 'get'
                },
                'pix_unlink_location_recurrence_automatic': {
                    'route': '/v2/locrec/:id/idRec',
                    'method': 'delete'
                },
                'pix_config_webhook_recurrence_automatic': {
                    'route': '/v2/webhookrec',
                    'method': 'put'
                },
                'pix_list_webhook_recurrence_automatic': {
                    'route': '/v2/webhookrec',
                    'method': 'get'
                },
                'pix_delete_webhook_recurrence_automatic': {
                    'route': '/v2/webhookrec',
                    'method': 'delete'
                },
                'pix_config_webhook_automatic_charge': {
                    'route': '/v2/webhookcobr',
                    'method': 'put'
                },
                'pix_list_webhook_automatic_charge': {
                    'route': '/v2/webhookcobr',
                    'method': 'get'
                },
                'pix_delete_webhook_automatic_charge': {
                    'route': '/v2/webhookcobr',
                    'method': 'delete'
                }
            }
        },
        'OPEN-FINANCE': {
            'URL': {
                'production': 'https://openfinance.api.efipay.com.br/v1',
                'sandbox': 'https://openfinance-h.api.efipay.com.br/v1'
            },
            'ENDPOINTS': {
                'authorize': {
                    'route': '/oauth/token',
                    'method': 'post'
                },
                'of_config_update': {
                    'route': '/config',
                    'method': 'put'
                },
                'of_config_detail': {
                    'route': '/config',
                    'method': 'get'
                },
                'of_devolution_pix': {
                    'route': '/pagamentos/pix/:identificadorPagamento/devolver',
                    'method': 'post'
                },
                'of_list_participants': {
                    'route': '/participantes/',
                    'method': 'get'
                }, 
                'of_start_pix_payment': {
                    'route': '/pagamentos/pix',
                    'method': 'post'
                },
                'of_list_pix_payment': {
                    'route': '/pagamentos/pix',
                    'method': 'get'
                },
                'of_cancel_schedule_pix': {
                    'route': '/pagamentos-agendados/pix/:identificadorPagamento/cancelar',
                    'method': 'patch'
                },
                'of_list_schedule_pix_payment': {
                    'route': '/pagamentos-agendados/pix',
                    'method': 'get'
                },
                'of_start_schedule_pix_payment': {
                    'route': '/pagamentos-agendados/pix',
                    'method': 'post'
                },
                'of_devolution_schedule_pix': {
                    'route': '/pagamentos-agendados/pix/:identificadorPagamento/devolver',
                    'method': 'post'
                },
                'of_start_recurrency_pix_payment': {
                    'route': '/pagamentos-recorrentes/pix',
                    'method': 'post'
                },
                'of_list_recurrency_pix_payment': {
                    'route': '/pagamentos-recorrentes/pix',
                    'method': 'get'
                },
                'of_cancel_recurrency_pix': {
                    'route': '/pagamentos-recorrentes/pix/:identificadorPagamento/cancelar',
                    'method': 'patch'
                },
                'of_devolution_recurrency_pix': {
                    'route': '/pagamentos-recorrentes/pix/:identificadorPagamento/devolver',
                    'method': 'post'
                },
                'of_replace_recurrency_pix_parcel': {
                    'route': '/pagamentos-recorrentes/pix/:identificadorPagamento/substituir/:endToEndId',
                    'method': 'patch'
                },
                'of_create_biometric_enrollment': {
                    'route': '/pagamentos-biometria/vinculos',
                    'method': 'post'
                },
                'of_list_biometric_enrollment': {
                    'route': '/pagamentos-biometria/vinculos',
                    'method': 'get'
                },
                'of_create_biometric_pix_payment': {
                    'route': '/pagamentos-biometria/pix',
                    'method': 'post'
                },
                'of_list_biometric_pix_payment': {
                    'route': '/pagamentos-biometria/pix',
                    'method': 'get'
                },
                'of_revoke_biometric_enrollment': {
                    'route': '/pagamentos-biometria/vinculos',
                    'method': 'patch'
                },
                'of_create_automatic_enrollment': {
                    'route': '/pagamentos-automaticos/adesao',
                    'method': 'post'
                },
                'of_list_automatic_enrollment': {
                    'route': '/pagamentos-automaticos/adesao',
                    'method': 'get'
                },
                'of_update_automatic_enrollment': {
                    'route': '/pagamentos-automaticos/adesao',
                    'method': 'patch'
                },
                'of_create_automatic_pix_payment': {
                    'route': '/pagamentos-automaticos/pix',
                    'method': 'post'
                },
                'of_list_automatic_pix_payment': {
                    'route': '/pagamentos-automaticos/pix',
                    'method': 'get'
                },
                'of_cancel_automatic_pix_payment': {
                    'route': '/pagamentos-automaticos/pix',
                    'method': 'patch'
                }
            }
        },
        'PAYMENTS': {
            'URL': {
                'production': 'https://pagarcontas.api.efipay.com.br/v1',
                'sandbox': ''
            },
            'ENDPOINTS':{
                'authorize': {
                    'route': '/oauth/token',
                    'method': 'post'
                },
                'pay_detail_bar_code': {
                    'route': '/codBarras/:codBarras',
                    'method': 'get'
                },
                'pay_request_bar_code': {
                    'route': '/codBarras/:codBarras',
                    'method': 'post'
                },
                'pay_detail_payment': {
                    'route': '/:idPagamento',
                    'method': 'get'
                },
                'pay_list_payments': {
                    'route': '/resumo',
                    'method': 'get'
                },
                'pay_config_webhook': {
                    'route': '/webhook',
                    'method': 'put'
                },
                'pay_delete_webhook': {
                    'route': '/webhook',
                    'method': 'delete'
                },
                'pay_list_webhook': {
                    'route': '/webhook',
                    'method': 'get'
                }
            }
        },
        'OPENING-ACCOUNTS': {
            'URL': {
                'production': 'https://abrircontas.api.efipay.com.br/v1',
                'sandbox': 'https://abrircontas-h.api.efipay.com.br/v1'
            },
            'ENDPOINTS': {
                'authorize': {
                    'route': '/oauth/token',
                    'method': 'post'
                },
                'create_account': {
                    'route': '/conta-simplificada',
                    'method': 'post'
                },
                'get_account_credentials': {
                    'route': '/conta-simplificada/:idContaSimplificada/credenciais',
                    'method': 'get'
                },
                'create_account_certificate': {
                    'route': '/conta-simplificada/:idContaSimplificada/certificado',
                    'method': 'post'
                },
                'account_config_webhook': {
                    'route': '/webhook',
                    'method': 'post'
                },
                'account_list_webhook': {
                    'route': '/webhooks',
                    'method': 'get'
                },
                'account_detail_webhook': {
                    'route': '/webhook/:identificadorWebhook',
                    'method': 'get'
                },
                'account_delete_webhook': {
                    'route': '/webhook/:identificadorWebhook',
                    'method': 'delete'
                }
            }
        },
        'STATEMENT': {
            'URL': {
                'production': 'https://extratos.api.efipay.com.br/v1',
                'sandbox': ''
            },
            'ENDPOINTS': {
                'authorize': {
                    'route': '/oauth/token',
                    'method': 'post'
                },
                'list_statement_files': {
                    'route': '/extrato-cnab/arquivos',
                    'method': 'get'
                },
                'get_statement_file': {
                    'route': '/extrato-cnab/download/:nome_arquivo',
                    'method': 'get'
                },
                'list_statement_recurrences': {
                    'route': '/extrato-cnab/agendamentos',
                    'method': 'get'
                },
                'create_statement_recurrency': {
                    'route': '/extrato-cnab/agendar',
                    'method': 'post'
                },
                'update_statement_recurrency': {
                    'route': '/extrato-cnab/agendar/:identificador',
                    'method': 'patch'
                },
                'create_sftp_key': {
                    'route': '/extrato-cnab/gerar-chaves',
                    'method': 'post'
                }
            }
        }
    }
